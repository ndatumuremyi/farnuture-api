from beanie import Document
from fastapi import UploadFile
from pydantic import BaseModel


class Category(Document):
    name: str
    image: str

    class Config:
        schema_extra = {
            "example": {
                "name": "a name",
                "image": "https://linktomyimage.com/image.png",
            }
        }

    class Settings:
        name = "categories"


class CreateCategory(BaseModel):
    name: str
    image: UploadFile
