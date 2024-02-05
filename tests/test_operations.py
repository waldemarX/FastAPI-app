from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post(
        "/operations/add",
        json={
            "quantity": "50.2",
            "figi": "code",
            "instrument_type": "bond",
            "type": "sell",
        },
    )

    assert response.status_code == 200, "Error creating operation"


async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get(
        "/operations/type",
        params={
            "operation_type": "sell",
        },
    )

    assert response.status_code == 200, "Error gettin operation"


async def test_get_all_operations(ac: AsyncClient):
    response = await ac.get(
        "/operations/all",
    )

    assert response.status_code == 200, "Error getting all operations"
