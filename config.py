import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '23qUoT6lmzPwXHfhfSQ3w141kXuLxI99h4jPOGxww141kXuLxI99h4jPOGxw'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True