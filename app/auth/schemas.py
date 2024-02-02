import uuid
from fastapi_users import models

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: models.ID
    username: str
    email: EmailStr
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    role_id: int
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


# class UserUpdate(schemas.BaseUserUpdate):
#     pass
