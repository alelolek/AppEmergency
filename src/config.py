class Config:
    SECRET_KEY = 'password1234'

class Developmentconfig(Config):
    DEBUG=True
    HOST = '...'
    USER = '...'
    PORT = ...
    PASSWORD = '...'
    DATABASE = '...'

config ={
    'development':Developmentconfig
}