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

def recuperarPorSetor(texto, orgao = 'UERR'):
    try:
        search = "%{}%".format(texto)
        lista = BemModel.query.filter_by(orgao=orgao).filter(BemModel.setor.ilike(search)).order_by(BemModel.descricao.asc()).all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista


def recuperarPorTombo(texto, orgao = 'UERR'):
    try:
        search = "%{}%".format(texto)
        lista = BemModel.query.filter_by(orgao=orgao).filter(BemModel.tombo.ilike(search)).order_by(BemModel.descricao.asc()).all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista
 

def recuperarPorDescricao(texto, orgao = 'UERR'):
    try:
        search = "%{}%".format(texto)
        lista = BemModel.query.filter_by(orgao=orgao).filter(BemModel.descricao.ilike(search)).order_by(BemModel.descricao.asc()).all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista
