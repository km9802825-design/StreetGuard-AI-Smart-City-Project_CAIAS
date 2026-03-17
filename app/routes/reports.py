from fastapi import APIRouter, UploadFile, File, Form
from app.utils.db import read_db, write_db
from app.services.file_service import save_image
router = APIRouter()

@router.post("/")
def create_report(
    lat: float = Form(...),
    lng: float = Form(...),
    type: str = Form(...),
    description: str = Form(...),
    image: UploadFile = File(None)
):
    db = read_db()

    image_path = None
    if image:
        image_path = save_image(image)

    report = {
        "lat": lat,
        "lng": lng,
        "type": type,
        "description": description,
        "image": image_path
    }

    db["reports"].append(report)
    write_db(db)

    return {"message": "Report submitted"}

@router.get("/")
def get_reports():
    return read_db()["reports"]