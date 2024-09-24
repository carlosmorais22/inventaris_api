from sqlalchemy import inspect

from ..app import db # from __init__.py

class SituationModel(db.Model):
    __tablename__ = 'situacao'
    __table_args__ = {'schema': 'inventaris'}

    id        = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    descricao = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, Situation):
        self.Situation = Situation

    def to_dict(self):
        return {
            "id" : self.id, 
            "descricao" : self.descricao
        }
