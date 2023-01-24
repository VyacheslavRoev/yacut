import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY', default='my_secret_key')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
BASE_DIR = Path(__file__).parent
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'