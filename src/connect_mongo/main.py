from fastapi import FastAPI
from routers import route_todo
from schemas import SuccessMsg

app = FastAPI()
app.include_router(route_todo.router)

@app.get("/", response_model=SuccessMsg)
def read_root():
    return { "message": "Welcome to FastAPI" }

@app.post("/test_gpt")
async def test_gpt(text: str):
    return {
        "message": f"{text}",
    }
