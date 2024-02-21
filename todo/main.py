from fastapi import FastAPI, APIRouter
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='todo/static'), name='static')
templates = Jinja2Templates(directory='todo/templates')