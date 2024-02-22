#импорты  fast_api
from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
#импорты  sqlalchemy
from sqlalchemy.orm import Session
#импорты  todo
from todo.database.base import get_db
from todo.models import ToDo
from todo.config import settings
#импорты  starlette
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND

router = APIRouter(
    tags=['ToDo - List']    # Добавляем квадратные скобки для списка тегов
)

templates = Jinja2Templates(directory="todo/templates")

@router.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('index.html',{'request': request,'app_name': settings.app_name,'todo_list': todos})

@router.post('/add/')
#три точки это означает что это строка
def add(title: str = Form(...), db_session: Session = Depends(get_db)):
    new_todo = ToDo(title=title)
    db_session.add(new_todo)
    db_session.commit()
    url = router.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@router.get('/update/{todo_id}')
def update(todo_id: int, db_session: Session = Depends(get_db)):
    todo = db_session.query(ToDo).filter(ToDo.id==todo_id).first()
    todo.is_complete = not todo.is_complete
    db_session.commit()
    url = router.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@router.get('/delete/{todo_id}')
def delete(todo_id : int, db_session : Session = Depends(get_db)):
    todo = db_session.query(ToDo).filter_by(id=todo_id).first()
    db_session.delete(ToDo)
    db_session.commit()
    url = router.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)