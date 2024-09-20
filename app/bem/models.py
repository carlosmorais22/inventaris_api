from sqlalchemy import inspect

from ..app import db # from __init__.py

class Bem(db.Model):
    __tablename__ = 'bem'
    __table_args__ = {'schema': 'inventaris'}

    id    = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    setor = db.Column(db.String(200), nullable=False)
    tombo = db.Column(db.String(50), nullable=False, unique=True)
    descricao = db.Column(db.String, nullable=False)
    conta = db.Column(db.String(12), nullable=False)
    estado = db.Column(db.String(7), nullable=False)
    valor = db.Column(db.Numeric(12,2), nullable=False)
    valor_remanescente = db.Column(db.Numeric(12,4), nullable=True)
    numero_serie = db.Column(db.String(30), nullable=False, unique=True)
    data = db.Column(db.DateTime, nullable=True)
    data_aquisicao = db.Column(db.DateTime, nullable=True)
    ativo = db.Column(db.SmallInteger, nullable=False)

    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.descricao