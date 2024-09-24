from sqlalchemy import inspect

from ..app import db # from __init__.py

class ContaModel(db.Model):
    __tablename__ = 'conta'
    __table_args__ = {'schema': 'inventaris'}

    id    = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    descricao = db.Column(db.String, nullable=False)
    tem_numero_serie = db.Column(db.Boolean, nullable=False)
    vida_util = db.Column(db.BigInteger, nullable=True)
    ativo = db.Column(db.Boolean, nullable=False)

    def __init__(self, Conta):
        self.Conta = Conta

    def to_dict(self):
        return {
            "id" : self.id, 
            "descricao" : self.descricao,
            "tem_numero_serie" : self.tem_numero_serie,
            "vida_util" : self.vida_util,
            "ativo" : self.ativo
        }
