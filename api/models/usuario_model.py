from sqlalchemy import inspect

from ..app import db # from __init__.py

class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'inventaris'}

    id    = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    modelo = db.Column(db.String(30), nullable=False)
    fabricante = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def __init__(self, Usuario):
        self.Usuario = Usuario

    def to_dict(self):
        return {
            "id" : self.id, 
            "nome" : self.nome,
            "cpf" : self.cpf,
            "modelo" : self.modelo,
            "fabricante" : self.fabricante,
            "status" : self.status,
        }
