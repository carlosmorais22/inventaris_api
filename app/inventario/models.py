from sqlalchemy import inspect
from datetime import datetime

from ..app import db # from __init__.py

class Inventario(db.Model):
    __tablename__ = 'inventario'
    __table_args__ = {'schema': 'inventaris'}

# Auto Generated Fields:
    id         = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update
    deleted_at = db.Column(db.DateTime(timezone=True))    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    ano = db.Column(db.SmallInteger, nullable=True)
    bem = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.SmallInteger, nullable=False)
    situacao = db.Column(db.SmallInteger, nullable=False)
    plaqueta = db.Column(db.Boolean, nullable=False)
    observacao = db.Column(db.String, nullable=True)
    cadastrado_por = db.Column(db.Integer, nullable=False)
    situacao_observacao = db.Column(db.String, nullable=True)
    tem_numero_serie = db.Column(db.Boolean, nullable=False)
    numero_serie = db.Column(db.String, nullable=True)

    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.descricao