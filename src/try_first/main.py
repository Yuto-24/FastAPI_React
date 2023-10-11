from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
import math

# cd src && uvicorn main:app

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
    shop_info:Optional[ShopInfo] = None
    items: List[Item]

app = FastAPI()


@app.get("/")
async def index():
    return {
        "message": "Working :D"
    }


@app.get("/hello")
async def index() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/countries/{country_name}")
async def country(country_name: str) -> dict[str, str]:
    return {"country_name": country_name}


@app.get("/studies")
async def study(name: Optional[str] = "math", no: Optional[int] = 0) -> dict:
    return {"study_name": name, "study_no": no}

@app.post("/item")
async def create_item(item: Item):
    return {
        "message": f"{item.name}は{math.ceil(item.price * item.tax)}円です。",
        "詳細": item.description,
    }

@app.get("/items")
async def create_item(data: Data):
    return {
        "message": "Working :D",
        "data": data
    }
