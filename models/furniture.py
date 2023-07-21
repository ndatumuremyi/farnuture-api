from typing import List

from beanie import Document, PydanticObjectId


class Furniture(Document):
    name: str
    images: List[str]
    category_id: PydanticObjectId

    class Config:
        schema_extra = {
            "example": {
                "name": "a name",
                "images": ["https://linktomyimage.com/image.png"],
                "category_id": "a categoryId"
            }
        }

    class Settings:
        name = "furniture"
