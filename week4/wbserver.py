import asyncio
import websockets

connected = set()

async def server(websocket, path):
    # Register.
    # 加入一個socket連線
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(f'Got a new MSG FOR YOU: {message}')
    finally:
        # Unregister.
        connected.remove(websocket)
    

start_server = websockets.serve(server, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

#https://www.youtube.com/watch?v=lv0oEnQY1pM&t=313s