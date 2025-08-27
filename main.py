from fastapi import FastAPI
from typing import Union
import asyncio
from app.bot import start_bot

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Запускаємо бота у фоні разом із FastAPI
@app.on_event("startup")
async def on_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
