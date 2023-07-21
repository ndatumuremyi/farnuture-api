from uuid import uuid4

from fastapi import UploadFile


async def save_image(image: UploadFile) -> str:
    unique_id = str(uuid4())
    filename = image.filename
    path = f"uploads/{unique_id}_{filename}"
    with open(path, "wb") as f:
        content = await image.read()
        f.write(content)

    return f"/{path}"
