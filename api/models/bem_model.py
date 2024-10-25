from sqlalchemy import inspect

from ..app import db # from __init__.py

class BemModel(db.Model):
    __tablename__ = 'bem'
    __table_args__ = {'schema': 'inventaris'}

    id    = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    setor = db.Column(db.String(200), nullable=False)
    tombo = db.Column(db.String(50), nullable=False, unique=True)
    descricao = db.Column(db.String, nullable=False)
    conta = db.Column(db.String(12), nullable=False)
    estado = db.Column(db.String(7), nullable=False)
    estado_descricao = db.Column(db.String(7), nullable=False)
    valor = db.Column(db.String, nullable=False)
    valor_remanescente = db.Column(db.Numeric(12,4), nullable=True)
    numero_serie = db.Column(db.String(30), nullable=False, unique=True)
    data = db.Column(db.DateTime, nullable=True)
    data_aquisicao = db.Column(db.DateTime, nullable=True)
    ativo = db.Column(db.SmallInteger, nullable=False)
    inventariado = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, Bem):
        self.Bem = Bem

    def to_dict(self):
        return {
            "id" : self.id, 
            "setor" : self.setor,
            "tombo" : self.tombo,
            "descricao" : self.descricao,
            "conta" : self.conta,
            "estado" : self.estado,
            "estado_descricao" : self.estado_descricao,
            "valor" : self.valor,
            "valor_remanescente" : self.valor_remanescente,
            "numero_serie" : self.numero_serie,
            "data" : self.data,
            "data_aquisicao" : self.data_aquisicao,
            "ativo" : self.ativo,
            "inventariado" : self.inventariado
        }
