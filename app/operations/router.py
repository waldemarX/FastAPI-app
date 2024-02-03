from fastapi import APIRouter, Depends
from sqlalchemy import insert
from .schemas import OperationCreate
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Operation


router = APIRouter(prefix="/operations", tags=["Operations"])


@router.get("/")
async def get_specific_operations(
    session: AsyncSession = Depends(get_async_session),
):
    query = select(Operation)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/")
async def add_specific_operations(
    new_operation: OperationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    statement = insert(Operation).values(**new_operation.model_dump())
    await session.execute(statement)
    await session.commit()
    return {"status": "success"}
