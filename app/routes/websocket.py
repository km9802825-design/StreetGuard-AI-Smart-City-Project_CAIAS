from fastapi import WebSocket

connected_clients = []

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except Exception:
        connected_clients.remove(websocket)

async def broadcast(message: dict):
    for client in connected_clients:
        await client.send_json(message)
