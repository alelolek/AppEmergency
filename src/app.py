from flask import Flask, render_template, request,redirect,url_for,flash
from config import config
from flask_login import LoginManager,login_user,logout_user,login_required
# from flask_wtf.csrf import CSRFProtect

from models.modelUsers import ModelUser

from models.entities.Users import User

app =Flask(__name__)

# csrf= CSRFProtect()
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def loaderUser(id):
    return ModelUser.getId(id)




# LOGIN


@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0,request.form['username'],request.form['password'])
        loggedUser =ModelUser.login(user)
        if loggedUser != None:
            if loggedUser.password:
                login_user(loggedUser)
                return redirect(url_for('ver'))
            else:
                flash("password invalid...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


# @app.route("/home")
# def home():
#     return render_template('home.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/protected')
@login_required
def protected():
    return " <h1>Esta es una vista protegida</h1>"



# PAGINA PRINCIPAL
from database.conexion  import conexion
from models.modelAd import ModelAddmiter
from models.entities.Addmiter import Admited

@app.route("/ver")
def ver():
    ent=[]
    Entrantes = ModelAddmiter.ver(ent)
    return render_template("ver.html", ent = Entrantes)


@app.route("/add",methods=['GET','POST'])
def añadir():
    if request.method == 'GET':
        e = {"id":0,"nombre":'',"apellido":'',"motivo":'',"fecha":'',"hora":''}
        return render_template("add.html", ent = e)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        motivo = request.form['motivo']
        fecha = request.form['fecha']
        hora = request.form['hora']
        datos = nombre,apellido,motivo,fecha,hora
        ModelAddmiter.add(datos)
        return redirect('/ver')


@app.route('/actualizar/<int:id>',methods=['GET','POST'])
def actualizar(id):
    e = {}
    conn = conexion()
    cursor = conn.cursor()
    if request.method == 'GET':
        sentenciaSQL = '''SELECT * FROM ingresados WHERE id=%s'''
        cursor.execute(sentenciaSQL,(str(id)))
        for row in cursor.fetchall():
            e = {"id":row[0],"nombre":row[1],"apellido":row[2],"motivo":row[3],"fecha":row[4],"hora":row[5]}
        conn.close()
        return render_template('add.html', ent=e)
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        apellido = str(request.form['apellido'])
        motivo = str(request.form['motivo'])
        fecha = str(request.form['fecha'])
        hora = str(request.form['hora'])
        sentenciaSQL = '''UPDATE ingresados SET  nombre = %s, apellido = %s, motivo = %s, fecha = %s, hora = %s WHERE id = %s'''
        cursor.execute(sentenciaSQL,(nombre,apellido,motivo,fecha,hora,str(id)))
        conn.commit()
        conn.close()
        return redirect('/ver')


@app.route('/eliminar/<int:id>')
def eliminar(id):
    ModelAddmiter.delete(id)
    return redirect('/ver')



def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Pagina no encontrada</h1>",404


if __name__=='__main__':
    app.config.from_object(config['development'])
    # csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()

