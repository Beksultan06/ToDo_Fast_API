from fastapi import APIRouter, Depends, Request, FastAPI
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from todo.database.base import get_db
from todo.models import ToDo
from todo.config import settings

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'todo_list': todos}
                                       )
