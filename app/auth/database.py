from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import (
    SQLAlchemyUserDatabase,
)
from fastapi_users_db_sqlalchemy import UUID_ID, SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.generics import GUID
import uuid
from sqlalchemy import TIMESTAMP, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import DB_PASSWORD, DB_USERNAME
from models.base import Base

DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@localhost/test"
)


class User(SQLAlchemyBaseUserTableUUID, Base):
    id: Mapped[UUID_ID] = mapped_column(
        GUID, primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(
        String(length=150), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, nullable=False
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("role.id")
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    registred_at: Mapped[str] = mapped_column(
        TIMESTAMP, default=datetime.utcnow(), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
