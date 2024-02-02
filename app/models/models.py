from sqlalchemy import JSON, Column, Integer, String
from auth.database import User

from models.base import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class UserTable(User):
    ...
