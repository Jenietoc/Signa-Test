import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATA_BASE_URL")
    FLASK_ENV = os.getenv("FLASK_ENV")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
