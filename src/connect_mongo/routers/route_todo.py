from typing import Union
from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas import Todo, TodoBody
from database import db_create_todo
from starlette.status import HTTP_201_CREATED

router = APIRouter()


# response_model で返すレスポンスの型を指定する
@router.post("/api/todo", response_model = Todo)
async def create_todo(request: Request, response: Response, data: TodoBody) -> Union[dict, bool]:
    todo = jsonable_encoder(data)
    res = await db_create_todo(todo)
    response.status_code = HTTP_201_CREATED

    if res:
        return res
    raise HTTPException(
        status_code=404, detail="Create task failed"
    )
