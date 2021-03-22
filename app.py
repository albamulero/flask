from flask import Flask
from flask import request  
from flask import render_template
from flask import g
from flask import url_for
from flask import redirect
from flask_wtf import CsrfProtect
from config import DevelopmenConfig
from models import db
from models import User

# Importamos el archivo que contiene el formulario form.py
import form


app = Flask(__name__)
app.config.from_object(DevelopmenConfig)
app.secret_key = app.secret_key
csrf = CsrfProtect(app)


@app.route('/', methods=['GET', 'POST'])  
def index():

    usuario_form = form.UsuariosForm(request.form)
    usuarios = User.query.all()

    print(usuarios)
    
    return render_template('index.html', form  = usuario_form, usuarios = usuarios)

@app.route('/create', methods=['POST'])  
def create():

    create_form = form.UsuariosForm(request.form)

    if request.method == 'POST' and create_form.validate():

        usuario = User( num_serie = create_form.num_serie.data,
                        nombre = create_form.nombre.data,
                        apellido = create_form.apellido.data,
                        movil = create_form.movil.data,
                        email = create_form.email.data,
                        provincia = create_form.provincia.data,
                        pais = create_form.pais.data)

        db.session.add(usuario)
        try:
            db.session.commit()
            success = 'Registro añadido correctamente'
            return redirect("/ver")
        except:
            print('Error en la base de datos...')
            success = 'No se puedo actualizar la base de datos'

        finally:
            pass



        usuario_form = form.UsuariosForm(request.form)
    return render_template('index.html', form  = usuario_form, mensaje = success)


@app.route('/ver', methods=['GET'])  
def ver_usuarios():

    usuarios = User.query.all()
    
    return render_template('ver_usuarios.html', usuarios = usuarios)
     


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
