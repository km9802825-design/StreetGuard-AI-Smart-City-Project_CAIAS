from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from app.routes.websocket import broadcast

router = APIRouter()

# Request model
class SOSRequest(BaseModel):
    user: str
    location: str
    message: str

@router.post("/")
def send_sos(data: SOSRequest):
    sos_data = {
        "user": data.user,
        "location": data.location,
        "message": data.message,
        "time": str(datetime.now())
    }

    # 🔥 Broadcast to all connected clients
    broadcast(sos_data)

    return {
        "status": "SOS Sent 🚨",
        "data": sos_data
    }