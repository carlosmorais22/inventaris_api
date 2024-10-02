from flask import request, jsonify
import uuid

from ..app import db
from ..models.bem_model import BemModel
from ..entities.bem import Bem

def list():
    try:
        lista = BemModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def recuperar(id):
    response = BemModel.query.get(id).toDict()
    return jsonify(response)

def recuperarPorSetor(texto):
    search = "%{}%".format(texto)
    return BemModel.query.filter(BemModel.setor.ilike(search))

def recuperarPorTombo(texto):
    search = "%{}%".format(texto)
    return BemModel.query.filter(BemModel.tombo.ilike(search))

def recuperarPorDescricao(texto):
    search = "%{}%".format(texto)
    return BemModel.query.filter(BemModel.descricao.ilike(search))

