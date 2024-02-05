from fastapi import APIRouter, Depends
from sqlalchemy import insert
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi_cache.decorator import cache

from .models import Operation
from .schemas import OperationCreate
from base_responses import response_error, response_ok

from asyncio import sleep


router = APIRouter()


@router.get("/all")
async def get_all_operations(
    limit: int = 10,
    offset: int = 0,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(Operation).limit(limit).offset(offset)
        result = await session.execute(query)
        return response_ok(data=result.scalars().all())
    except Exception:
        return response_error()


@router.get("/type")
async def get_specific_operations(
    operation_type: str,
    session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(Operation).where(Operation.type == operation_type)
        result = await session.execute(query)
        return response_ok(data=result.scalars().all())
    except Exception:
        return response_error()


@router.post("/add")
async def add_specific_operations(
    new_operation: OperationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    statement = insert(Operation).values(**new_operation.model_dump())
    await session.execute(statement)
    await session.commit()
    return response_ok(data="Operation successfully added!")


@router.get("/long_operation")
@cache(expire=30)
async def get_long_op():
    await sleep(3)
    return response_ok(data="very long crud operation done!")
