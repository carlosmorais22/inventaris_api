from sqlalchemy import inspect
from datetime import datetime

from ..app import db # from __init__.py

class InventoryModel(db.Model):
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
    plaqueta = db.Column(db.SmallInteger, nullable=False, server_default="false")
    observacao = db.Column(db.String, nullable=True)
    cadastrado_por = db.Column(db.Integer, nullable=False)
    situacao_observacao = db.Column(db.String, nullable=True)
    tem_numero_serie = db.Column(db.SmallInteger, nullable=False, server_default="false")
    numero_serie = db.Column(db.String, nullable=True)

    def __init__(self, inventory):
        self.ano=inventory.ano,
        self.bem=inventory.bem,
        self.estado=inventory.estado,
        self.situacao=inventory.situacao,
        self.plaqueta=inventory.plaqueta,
        self.observacao=inventory.observacao,
        self.cadastrado_por=inventory.cadastrado_por,
        self.situacao_observacao=inventory.situacao_observacao,
        self.tem_numero_serie=inventory.tem_numero_serie,
        self.numero_serie=inventory.numero_serie

    def to_dict(self):
        return {
            "id" : self.id, 
            "ano" : self.ano,
            "bem" : self.bem,
            "estado" : self.estado,
            "situacao" : self.situacao,
            "plaqueta" : self.plaqueta,
            "observacao" : self.observacao,
            "cadastrado_por" : self.cadastrado_por,
            "situacao_observacao" : self.situacao_observacao,
            "tem_numero_serie" : self.tem_numero_serie,
            "numero_serie" : self.numero_serie,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at,
            "deleted_at" : self.deleted_at,
        }
