from uuid import uuid4

from fastapi import APIRouter, Form, UploadFile

from database.connection import Database
from models.categories import Category

category_router = APIRouter(tags=["Categories"])

category_database = Database(Category)


@category_router.get("")
@category_router.get("/")
async def get_user_by_id() -> list[Category]:
    return await category_database.get_all()


@category_router.post("/")
@category_router.post("")
async def create_category(name: str = Form(...), image: UploadFile = Form(...)) -> dict:
    unique_id = str(uuid4())
    filename = image.filename
    path = f"uploads/{unique_id}_{filename}"
    with open(path, "wb") as f:
        content = await image.read()
        f.write(content)

    _category = Category(
        name=name,
        image=f"/{path}"
    )
    await category_database.save(_category)
    return {
        "detail": "Category created successfully"
    }
