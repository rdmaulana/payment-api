import pytest
import os

from app import create_app
from flask_pymongo import PyMongo

mongo = PyMongo()

@pytest.fixture(scope='module', autouse=True)
def flask_app():
    app_settings = os.getenv(
        'APP_SETTINGS',
        'app.config.TestingConfig'
    )
    app = create_app()
    app.config.from_object(app_settings)

    return app

# @pytest.fixture(scope='module', autouse=True)
# def app_context(flask_app):
#     payload = {
#         "first_name": "Arnold",
#         "last_name": "Purnomo",
#         "phone_number" : "085781930218", 
#         "address": "Jl. Bandung Raya No. 55", 
#         "pin": "123456"
#     }

#     with flask_app.app_context():
#         mongo.init_app(app=flask_app)
#         mongo.db.users.insert_one(payload)
#         yield
#         mongo.db.users.drop()


@pytest.fixture(scope='module', autouse=True)
def test_client(flask_app):
    with flask_app.test_client() as testing_client:
        mongo.init_app(app=flask_app)
        with flask_app.app_context():
            yield testing_client
            mongo.db.users.drop()

# @pytest.fixture
# def init_user():
#     payload = {
#         "first_name": "Arnold",
#         "last_name": "Purnomo",
#         "phone_number" : "085781930218", 
#         "address": "Jl. Bandung Raya No. 55", 
#         "pin": "123456"
#     }
#     return payload

# @pytest.fixture
# def init_database(test_client, init_user):
#     user = init_user
#     mongo.db.users.insert_one(user)

#     yield

#     mongo.db.users.drop()



