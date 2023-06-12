from typing import List

from fastapi import APIRouter
from fastapi import Depends

from auth.authenticate import require_role
from database.connection import Database
from models.users import User

user_router = APIRouter(tags=["Users"])

user_database = Database(User)


@user_router.get("/")
async def retrieve_all_users(_=Depends(require_role("ADMIN"))) -> List[User]:
    users = await user_database.get_all()
    return users


@user_router.get("/{id_}")
async def get_user_by_id(id_, _=Depends(require_role("ADMIN"))) -> User:
    user = await user_database.get(id_)
    return user
