import os
from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from app.routes.websocket import broadcast

try:
    from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
except Exception:
    ConnectionConfig = None
    FastMail = None
    MessageSchema = None

router = APIRouter()

class SOSRequest(BaseModel):
    user: str
    location: str
    message: str


@router.post("/")
async def send_sos(data: SOSRequest):
    sos_data = {
        "user": data.user,
        "location": data.location,
        "message": data.message,
        "time": str(datetime.now())
    }
    mail_username = os.getenv("MAIL_USERNAME")
    mail_password = os.getenv("MAIL_PASSWORD")
    mail_from = os.getenv("MAIL_FROM")
    mail_recipient = os.getenv("MAIL_RECIPIENT", "km9802825@gmail.com")
    mail_server = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    mail_port = int(os.getenv("MAIL_PORT", "587"))
    email_status = {
        "enabled": False,
        "sent": False,
        "recipient": mail_recipient,
        "detail": ""
    }

    if not (ConnectionConfig and FastMail and MessageSchema):
        email_status["detail"] = "fastapi-mail is not installed"
    else:
        missing_fields = []
        if not mail_username:
            missing_fields.append("MAIL_USERNAME")
        if not mail_password:
            missing_fields.append("MAIL_PASSWORD")
        if not mail_from:
            missing_fields.append("MAIL_FROM")
        if not mail_recipient:
            missing_fields.append("MAIL_RECIPIENT")
        if missing_fields:
            email_status["detail"] = f"Missing env config: {', '.join(missing_fields)}"
        else:
            email_status["enabled"] = True
            try:
                conf = ConnectionConfig(
                    MAIL_USERNAME=mail_username,
                    MAIL_PASSWORD=mail_password,
                    MAIL_FROM=mail_from,
                    MAIL_PORT=mail_port,
                    MAIL_SERVER=mail_server,
                    MAIL_STARTTLS=True,
                    MAIL_SSL_TLS=False,
                    USE_CREDENTIALS=True
                )
                message = MessageSchema(
                    subject="SOS ALERT",
                    recipients=[mail_recipient],
                    body=f"User: {data.user}\nLocation: {data.location}\nMessage: {data.message}\nTime: {sos_data['time']}",
                    subtype="plain"
                )
                fm = FastMail(conf)
                await fm.send_message(message)
                email_status["sent"] = True
                email_status["detail"] = "Email delivered"
            except Exception as exc:
                email_status["detail"] = str(exc)

    try:
        await broadcast({"type": "SOS", "data": sos_data})
    except Exception:
        pass

    return {
        "status": "SOS Sent 🚨",
        "data": sos_data,
        "email": email_status
    }
