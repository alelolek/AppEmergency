from .entities.Users import User
from database.conexion  import conexion

class ModelUser():

    @classmethod
    def login(self,user):
        try:
            conn= conexion()
            cursor = conn.cursor()
            sql = """SELECT id,username,password,fullname FROM users WHERE username= '{}' """.format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password),row[3])
                return user
            else:
                return None
        except Exception as err:
            raise Exception(err)




    @classmethod
    def getId(self,id):
        try:
            conn= conexion()
            cursor = conn.cursor()
            sql = """SELECT id,username,fullname FROM users WHERE id= {} """.format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None,row[2])
                
            else:
                return None
        except Exception as err:
            raise Exception(err)
