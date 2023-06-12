from typing import Optional

from beanie import Document
from bson import ObjectId
from pydantic import BaseModel, EmailStr

from models.parties.user_roles import UserRole


class User(Document):
    _id: Optional[ObjectId]
    email: EmailStr
    password: str
    firstName: str
    lastName: str
    role: UserRole = UserRole.USER

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "firstName": "Paterne",
                "lastName": "NDATUMUREMYI",
                "role": "USER"
            }
        }

    @property
    def id(self):
        return self._id


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
