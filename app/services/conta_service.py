from flask import request, jsonify
import uuid

from ..app import db
from ..models.conta_model import ContaModel

def list():
    try:
        lista = ContaModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def retrieve(id):
    response = ContaModel.query.get(id).toDict()
    return jsonify(response)
