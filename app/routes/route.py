from fastapi import APIRouter
from app.services.route_service import get_safe_route
router = APIRouter()

@router.get("/")
def route(start: str, end: str):
    return get_safe_route(start, end)