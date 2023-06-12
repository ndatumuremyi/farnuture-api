from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
import uvicorn

app = FastAPI()

# Register routes
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


# @app.get("/")
# async def root() -> dict:
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str) -> dict:
#     return {"message": f"Hello {name}"}
