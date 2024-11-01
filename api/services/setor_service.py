from flask import jsonify
from ..models.setor_model import SetorModel

def list(orgao='UERR'):
    try:
        lista = SetorModel.query.filter_by(orgao=orgao).all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista


def recuperar(id):
    response = SetorModel.query.get(id).toDict()
    return jsonify(response)
