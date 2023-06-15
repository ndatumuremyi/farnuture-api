from fastapi import APIRouter
from fastapi import Depends

from auth.authenticate import authenticate
from database.connection import Database
from models.users import User

profile_router = APIRouter(tags=["Profile"])

user_database = Database(User)


@profile_router.get("/")
async def get_user_by_id(user_info: dict = Depends(authenticate)) -> User:
    user = await user_database.get(user_info.get("userId"))
    return user
