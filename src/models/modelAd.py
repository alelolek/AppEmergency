from .entities.Addmiter import Admited
from database.conexion  import conexion
from models.entities.Addmiter import Admited

class ModelAddmiter():

    @classmethod
    def ver(self,ent):
        try:
            conn = conexion()
            cursor = conn.cursor()
            sentenciaSQL = '''SELECT * FROM ingresados ORDER BY id'''
            cursor.execute(sentenciaSQL)
            for row in cursor.fetchall():
                ent.append({"id":row[0],"nombre": row[1],"apellido":row[2],"motivo":row[3],"fecha":row[4],"hora":row[5]})
                conn.close()
            return ent
        except Exception as err:
            raise Exception(err)


    @classmethod
    def add(self,datos):
        conn = conexion()
        cursor = conn.cursor()
        sentenciaSQL = '''INSERT INTO ingresados(nombre,apellido,motivo,fecha,hora) VALUES(%s,%s,%s,%s,%s)'''
        cursor.execute(sentenciaSQL,datos)
        conn.commit()
        conn.close()

    @classmethod
    def update(self,id):
        conn = conexion()
        cursor = conn.cursor()



    @classmethod
    def delete(self,id):
        conn = conexion()
        cursor = conn.cursor()
        sentenciaSQL = '''DELETE FROM ingresados WHERE id =  %s'''
        cursor.execute(sentenciaSQL,(str(id)))
        conn.commit()
        conn.close()