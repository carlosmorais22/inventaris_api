from flask import request, jsonify
import uuid

from ..app import db
from ..models.bem_model import BemModel

def list():
    try:
        lista = BemModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def retrieve(id):
    response = BemModel.query.get(id).toDict()
    return jsonify(response)
