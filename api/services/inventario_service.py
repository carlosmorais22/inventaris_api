from flask import request, jsonify
import uuid

from ..app import db
from ..models.inventario_model import InventarioModel

def recuperar(id):
    response = InventarioModel.query.get(id).toDict()
    return jsonify(response)

def list():
    try:
        lista = InventarioModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def create(item):
    model = InventarioModel(item)

    db.session.add(model)
    db.session.commit()
    return model
