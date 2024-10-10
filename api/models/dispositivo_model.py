from sqlalchemy import inspect

from ..app import db # from __init__.py

class DispositivoModel(db.Model):
    __tablename__ = 'dispositivo'
    __table_args__ = {'schema': 'inventaris'}

    id    = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    modelo = db.Column(db.String(30), nullable=False)
    fabricante = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    is_adm = db.Column(db.Boolean, nullable=False)

    def __init__(self, dispositivo):
        self.id=dispositivo.id,
        self.nome=dispositivo.nome,
        self.cpf=dispositivo.cpf,
        self.modelo=dispositivo.modelo,
        self.fabricante=dispositivo.fabricante,
        self.status=dispositivo.status
        self.is_adm=dispositivo.is_adm

    def to_dict(self):
        return {
            "id" : self.id, 
            "nome" : self.nome,
            "cpf" : self.cpf,
            "modelo" : self.modelo,
            "fabricante" : self.fabricante,
            "status" : self.status,
            "is_adm" : self.is_adm,
        }
