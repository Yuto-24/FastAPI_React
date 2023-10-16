from fastapi import FastAPI
from use_langchain import create_summarize, create_summarize_md, create_summarize_md_using_OutputParser, create_section_title


app = FastAPI()
# app.include_router(router_todo.router)

@app.get("/")
async def root():
    return { "message": "It's Work :)" }

@app.post("/gpt/summarize")
async def summarize(text: str):
    return {
        # "input": text,
        "output": create_summarize(text).content
    }


@app.post("/gpt/summarize_md")
async def output_with_md(text: str):
    return {
        # "input": text,
        "output": create_summarize_md(text).content
    }

@app.post("/gpt/md_using_OutputParser")
async def summarize_md_using_OutputParser(text: str):
    return {
        # "input": text,
        "output": create_summarize_md_using_OutputParser(text)
    }

@app.post("/gpt/make_section_title")
async def make_section_title(text: str):
    return {
        "output": create_section_title(text).content
    }
