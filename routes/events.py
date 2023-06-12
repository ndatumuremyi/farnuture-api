from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(tags=["Events"])
events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.get("/{id_}", response_model=Event)
async def retrieve_event(id_: int) -> Event:
    for event in events:
        if event.id == id_:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully"
    }


@event_router.delete("/{id_}")
async def delete_event(id_: int) -> dict:
    for event in events:
        if event.id == id_:
            events.remove(event)
            return {"message": "Event deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }
