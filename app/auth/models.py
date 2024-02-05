from datetime import datetime
from fastapi_users_db_sqlalchemy import UUID_ID, SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.generics import GUID
import uuid
from sqlalchemy import JSON, TIMESTAMP, ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from base_class import Base


class Role(Base):
    __tablename__ = "role"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=120), nullable=False)
    permissions: Mapped[JSON] = mapped_column(JSON, nullable=True)


class User(SQLAlchemyBaseUserTableUUID, Base):
    __table_args__ = {'extend_existing': True}

    id: Mapped[UUID_ID] = mapped_column(
        GUID, primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(
        String(length=150), nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, nullable=False
    )
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))
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
