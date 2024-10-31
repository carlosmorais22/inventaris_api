from flask import request, jsonify
import uuid

from ..app import db
from ..models.dispositivo_model import DispositivoModel

def list():
    try:
        lista = DispositivoModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def recuperar(id):
    response = DispositivoModel.query.get(id)
    if (response != None):
        return response.to_dict()
    return None;

def recuperarPorIdMotivoFabricante(id, modelo, fabricante):
    response = DispositivoModel.query.filter_by(id=id).filter_by(modelo=modelo).filter_by(fabricante=fabricante).first()
    if (response != None):
        return response.to_dict()
    return None;

def create(item):
    model = DispositivoModel(item)

    db.session.add(model)
    db.session.commit()
    return model

def update(item):
    model = DispositivoModel(item)

    db.session.merge(model)
    db.session.commit()
    return model

