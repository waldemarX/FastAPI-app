from fastapi import WebSocket, WebSocketDisconnect, APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from base_responses import response_error, response_ok

from .models import Messages
from database import async_session_maker, get_async_session

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    @staticmethod
    async def add_messages_to_database(message: str):
        async with async_session_maker() as session:
            statement = insert(Messages).values(message=message)
            await session.execute(statement)
            await session.commit()


manager = ConnectionManager()


@router.get("/last_messages")
async def get_last_messages(
    session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(Messages).order_by(Messages.id.desc()).limit(5)
        messages = await session.execute(query)
        return response_ok(
            data=messages.scalars().all()[::-1], detail="Last 5 messages"
        )
    except Exception:
        return response_error()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            message = f"Client #{client_id} says: {data}"

            await manager.add_messages_to_database(message)
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
