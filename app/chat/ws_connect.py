"""
Example: connect to websocket using aiohttp
and write messages to txt file

Start server and execute this file "py ws_connect.py"
"""
import aiohttp
import time
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        #######
        client_id = int(time.time() * 1000)
        #######
        async with session.ws_connect(
            f"http://127.0.0.1:8000/chat/ws/{client_id}"
        ) as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_messages.txt", "a") as file:
                        file.write(f"{msg.data}\n")


asyncio.run(main())
