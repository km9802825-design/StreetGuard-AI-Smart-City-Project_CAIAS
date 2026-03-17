from fastapi import WebSocket

connected_clients = []

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except:
        connected_clients.remove(websocket)

def broadcast(message: dict):
    import asyncio
    for client in connected_clients:
        asyncio.create_task(client.send_json(message))