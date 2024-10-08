from sqlalchemy import inspect

from ..app import db # from __init__.py

class EstadoModel(db.Model):
    __tablename__ = 'estado'
    __table_args__ = {'schema': 'inventaris'}

    id        = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    descricao = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, Estado):
        self.Estado = Estado

    def to_dict(self):
        return {
            "id" : self.id, 
            "descricao" : self.descricao
        }
