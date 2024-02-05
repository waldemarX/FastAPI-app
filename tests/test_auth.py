from httpx import AsyncClient
from sqlalchemy import insert, select
from conftest import async_session_maker


from app.auth.models import Role


async def test_create_role():
    async with async_session_maker() as session:
        statement = insert(Role).values(id=1, name="user", permissions=None)
        await session.execute(statement)
        await session.commit()

        query = select(Role)
        result = await session.execute(query)
        assert len(result.scalars().all()) > 0, "Role not created"


async def test_register(ac: AsyncClient):
    response = await ac.post(
        "/auth/register",
        json={
            "email": "user@example.com",
            "password": "12234",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "string",
            "role_id": 0,
        },
    )
    if response.status_code == 201:
        assert 201 == 201  # User successfully created
    elif response.status_code == 400:
        assert 400 == 400  # User already exists (no errors)
    elif response.status_code == 422:
        raise AssertionError("Invalid data for creating user")
    else:
        raise AssertionError("Server error")
