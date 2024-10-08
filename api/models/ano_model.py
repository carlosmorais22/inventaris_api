from sqlalchemy import inspect

from ..app import db # from __init__.py

class AnoModel(db.Model):
    __tablename__ = 'ano'
    __table_args__ = {'schema': 'inventaris'}

    ano    = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    atual = db.Column(db.Boolean, nullable=False)

    def __init__(self, Ano):
        self.Ano = Ano

    def to_dict(self):
        return {
            "ano" : self.ano, 
            "atual" : self.atual
        }
