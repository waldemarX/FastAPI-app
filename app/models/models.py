from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from auth.database import User

from models.base import Base


class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=120), nullable=False)
    permissions: Mapped[JSON] = mapped_column(JSON, nullable=True)


class UserTable(User):
    pass
