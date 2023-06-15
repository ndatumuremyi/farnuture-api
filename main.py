from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse

from database.connection import Settings
from routes.auth import auth_router
from routes.categories import category_router
from routes.events import event_router
from routes.profile import profile_router
from routes.users import user_router

app = FastAPI()

settings = Settings()

# register origins

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes

app.include_router(auth_router, prefix="/auth")
app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/users")
app.include_router(profile_router, prefix="/profile")
app.include_router(category_router, prefix="/categories")


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


@app.get("/uploads/{image_path}")
def get_image(image_path: str):
    path = Path(f"uploads/{image_path}")
    image_extension = path.suffix.lower()
    media_type = f"image/{image_extension[1:]}"
    return FileResponse(path, media_type=media_type)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
