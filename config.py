import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'super_secret_key')
    ENVIRONMENT = os.getenv('ENV', 'development')
    if ENVIRONMENT == 'production':
        DB_USER = os.getenv('DB_USER', 'usuario_mysql')
        DB_PASS = os.getenv('DB_PASS', 'password_mysql')
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_NAME = os.getenv('DB_NAME', 'nombre_base')
        SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'aeropuertos.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
