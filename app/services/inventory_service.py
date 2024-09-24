from flask import request, jsonify
import uuid

from ..app import db
from ..models.inventory_model import InventoryModel

def retrieve(id):
    response = InventoryModel.query.get(id).toDict()
    return jsonify(response)

def list():
    try:
        lista = InventoryModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def create(item):
    model = InventoryModel(item)

    db.session.add(model)
    db.session.commit()
    return model
