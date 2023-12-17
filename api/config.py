import os

class Config:
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("AUTH_SECRET_KEY", "this-really-needs-to-be-changed")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://admin:password@localhost/auth-server")

    if SECRET_KEY == "this-really-needs-to-be-changed":
        print("DEFAULT SECRET KEY DETECTED!\nYou need to change the env variable AUTH_SECRET_KEY before deploying")

class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    JWT_ACCESS_TOKEN_EXPIRES = True

class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    JWT_ACCESS_TOKEN_EXPIRES = False

class TestingConfig(DevConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory"