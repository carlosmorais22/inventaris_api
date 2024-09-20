from sqlalchemy import inspect

from ..app import db # from __init__.py

class Estado(db.Model):
    __tablename__ = 'estado'
    __table_args__ = {'schema': 'inventaris'}

    id        = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    descricao = db.Column(db.String(50), nullable=False, unique=True)

    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.descricao