Простой ToDo менеджер, реализованный на веб-фреймворке FastAPI В качестве веб-интерфейса использован фреймворк Semantic UI https://semantic-ui.com/

Image alt

UPD 1.0 от 5.13.22

Добавлен файл config.py и туда перенесена конфигурация приложения
Добавлен модуль python-dotenv и файл .env для хранения значений переменных окружения приложения
Внимание! Файл .env должен быть указан в файле .gitignore чтобы ваши настройки не улетели в репозиторий Для данного примера я его исключил из файла игнора

Создаем папку для нового проекта и переходим в нее

md ToDoFastAPI & cd ToDoFastAPI
Устанавливаем и активируем виртуальное окружение

python3 -m venv venv
. venv/bin/activate
Структура файлов и папок

md todo & cd todo
mkdir templates\todo
mkdir static\css
echo .> static/css/style.css
echo .> .gitignore
echo .> README.MD
    
echo .> __init__.py
md database
echo .> database/__init__.py
echo .> database/base.py
echo .> models.py
echo .> config.py
echo .> app.py
echo .> routes.py
echo .> templates/todo/layout.html
echo .> templates/todo/index.html 
cd ..
echo .> main.py
Чтобы автоматически создать структуру проекта запустите в консоли файл

fastapi_structure_project.bat
Инициализируем git

git init
Устанавливаем модули

pip install fastapi uvicorn sqlalchemy jinja2
pip install python-multipart python-dotenv
Или установить полный fastapi, включающий jinja2, python-multipart, uvicorn

pip install fastapi[all] sqlalchemy
Создаем файл с зависимостями проекта

pip freeze > requirements.txt
База данных должна быть в файле .gitignore, но для этого примера я ее оттуда удалил, чтобы был пример ToDo задач

Запускаем приложение

run - файл run.py, содержащий объект приложения app

uvicorn main:app --reload --port 5000