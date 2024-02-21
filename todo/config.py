from pydantic_settings import BaseSettings

import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_name: str = os.getenv('NAME_APP')
    db_url: str = os.getenv('SQLALCHEMY_DATABASE_URL')

    class Config:
        env_file: str = '../.env'

settings = Settings()
