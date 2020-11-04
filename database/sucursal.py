from .db import db

class Sucursal(db.Document):
    sucursal_id = db.StringField(required=True, unique=True)
    nombre = db.StringField(required=True)
    direccion = db.StringField(required=True)
    telefono = db.StringField(required=True)
    preexistence = db.ListField(db.StringField(), required=True)
