from typing import List

from fastapi import APIRouter, Form, UploadFile

from database.connection import Database
from models.furniture import Furniture
from utils.imageUtils import save_image

furniture_route = APIRouter(tags=["Furniture"])

furniture_database = Database(Furniture)


@furniture_route.get("")
@furniture_route.get("/")
async def get_furniture() -> list[Furniture]:
    return await furniture_database.get_all()


@furniture_route.post("/")
@furniture_route.post("")
async def create_category(name: str = Form(...), category_id: str = Form(...),
                          images: List[UploadFile] = Form(...)) -> dict:
    image_list = []
    for image in images:
        image_list.append(await save_image(image))

    furniture = Furniture(
        name=name,
        category_id=category_id,
        images=image_list
    )
    await furniture_database.save(furniture)
    return {
        "detail": "furniture created successfully"
    }
