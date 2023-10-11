from fastapi import FastAPI
from use_langchain import create_summarize


app = FastAPI()
# app.include_router(router_todo.router)

@app.get("/")
async def root():
    return { "message": "It's Work :)" }

@app.post("/gpt")
async def test(text: str):
    return {
        "input": text,
        "output": create_summarize(text).content
    }
