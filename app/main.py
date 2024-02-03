import uuid
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from models.models import UserTable

from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead

app = FastAPI(title="Trading App")

fastapi_users = FastAPIUsers[UserTable, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
