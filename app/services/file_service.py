import shutil

def save_image(file):
    path = f"app/uploads/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return path