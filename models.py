from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.Integer, primary_key=True)
    num_serie = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    movil = db.Column(db.String(50))
    email = db.Column(db.String(50))
    provincia = db.Column(db.String(50))
    pais = db.Column(db.String(50))
