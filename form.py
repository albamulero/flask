from wtforms import Form
from wtforms import StringField, TextField, validators
from wtforms.fields.html5 import EmailField

class UsuariosForm(Form):
    num_serie = StringField('Numero de serie',[validators.Required(message="El numero de serie es requerido")])
    nombre = StringField('Nombre',[
        validators.length(min=4, max=50, message="Ingrese un nombre valido")
    ])
    apellido = StringField('Apellido')
    movil = StringField('Movil')
    email = EmailField('Correo electronico',
        [validators.Required(message="El emal es requerido"), validators.Email(message='Ingrese un email valido')])
    provincia = StringField('Provincia')
    pais = StringField('Pais')