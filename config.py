import os

class Config(object):
    SECRET_KEY = 'alba'

class DevelopmenConfig(Config):
    DEBUG = True,
    HOST = '0.0.0.0',
    port = '3000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///usuarios.sqlite'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'alba'
    
    