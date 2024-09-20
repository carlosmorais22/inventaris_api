from flask import request, jsonify
import uuid

from ..app import db
from ..models.situacao_model import SituacaoModel

def list():
    try:
        lista = SituacaoModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def retrieve(id):
    response = SituacaoModel.query.get(id).toDict()
    return jsonify(response)
