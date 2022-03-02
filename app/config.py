import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(dirname(__file__), './../.env')
load_dotenv(dotenv_path)

class BaseConfig(object):
    DEBUG = False
    JWT_SECRET_KEY = os.environ['SECRET_KEY']
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    REDISTOGO_URL = os.environ['REDIS_URL']
    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
    CSRF_ENABLED = True
    BCRYPT_HASH_PREFIX = 14
    BCRYPT_LOG_ROUNDS = 12
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECONDS = 3000

class DevelopmentConfig(BaseConfig):
    MONGO_URI = os.environ['DATABASE_URL']
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    MONGO_URI = os.environ['DATABASE_TEST_URL']
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=5)

class ProductionConfig(BaseConfig):
    DEBUG = False
