from fastapi import APIRouter
from app.utils.db import read_db

router = APIRouter()

@router.get("/")
def dashboard():
    db = read_db()

    return {
        "total_reports": len(db["reports"]),
        "total_users": len(db["users"]),
        "status": "Active"
    }