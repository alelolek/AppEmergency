from config import Developmentconfig
from psycopg2 import connect


def conexion():
    host= Developmentconfig.HOST
    port = Developmentconfig.PORT
    user= Developmentconfig.USER
    password= Developmentconfig.PASSWORD
    database=Developmentconfig.DATABASE
    db = connect(host=host,port=port,database=database,user=user,password=password)
    return db
