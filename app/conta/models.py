from sqlalchemy import inspect

from ..app import db # from __init__.py

class Conta(db.Model):
    __tablename__ = 'conta'
    __table_args__ = {'schema': 'inventaris'}

    id    = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    descricao = db.Column(db.String, nullable=False)
    tem_numero_serie = db.Column(db.Boolean, nullable=False)
    vida_util = db.Column(db.BigInteger, nullable=True)
    ativo = db.Column(db.Boolean, nullable=False)

    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.descricao