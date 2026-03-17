from fastapi import APIRouter
from app.utils.db import read_db, write_db

router = APIRouter()

@router.post("/signup")
def signup(user: dict):
    db = read_db()
    db["users"].append(user)
    write_db(db)
    return {"message": "User created"}

@router.post("/login")
def login(user: dict):
    db = read_db()
    for u in db["users"]:
        if u["email"] == user["email"]:
            return {"message": "Login success"}
    return {"error": "Invalid credentials"}