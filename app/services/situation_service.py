from flask import request, jsonify
import uuid

from ..app import db
from ..models.situation_model import SituationModel

def list():
    try:
        lista = SituationModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def retrieve(id):
    response = SituationModel.query.get(id).toDict()
    return jsonify(response)

def create(item):
    model = SituationModel(item)

    db.session.add(model)
    db.session.commit()
    return model
