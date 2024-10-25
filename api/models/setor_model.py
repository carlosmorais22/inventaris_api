from sqlalchemy import inspect

from ..app import db # from __init__.py

class SetorModel(db.Model):
    __tablename__ = 'setor'
    __table_args__ = {'schema': 'inventaris'}

    id    = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    nome = db.Column(db.String, nullable=False)
    sigla = db.Column(db.String, nullable=False)

    def __init__(self, Setor):
        self.Setor = Setor

    def to_dict(self):
        return {
            "id" : self.id, 
            "nome" : self.nome,
            "sigla" : self.sigla
        }
