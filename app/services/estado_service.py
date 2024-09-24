from flask import request, jsonify
import uuid

from ..app import db
from ..models.estado_model import EstadoModel

def list():
    try:
        lista = EstadoModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def retrieve(id):
    response = EstadoModel.query.get(id).toDict()
    return jsonify(response)
