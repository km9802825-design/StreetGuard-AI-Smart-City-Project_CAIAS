from fastapi import FastAPI
from fastapi import WebSocket
from app.routes import auth, reports, route, dashboard, emergency
from app.routes.websocket import websocket_endpoint
app = FastAPI(title="StreetGuard AI")

app.include_router(auth.router, prefix="/auth")
app.include_router(reports.router, prefix="/reports")
app.include_router(route.router, prefix="/route")
app.include_router(dashboard.router, prefix="/dashboard")
app.include_router(emergency.router, prefix="/emergency")

@app.get("/")
def home():
    return {"message": "StreetGuard AI Backend Running 🚀"}
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)