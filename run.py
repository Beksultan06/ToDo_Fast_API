from todo.main import app
from todo.routes import router

app.include_router(router)
