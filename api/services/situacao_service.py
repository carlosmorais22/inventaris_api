from flask import jsonify
from ..app import db
from ..models.situacao_model import SituacaoModel


def list():
    try:
        lista = SituacaoModel.query.all()
    except UnicodeDecodeError as e:
        return f"Erro: {e}"
    except Exception as e:
        return f"Erro: {e}"
    return lista


def recuperar(id):
    response = SituacaoModel.query.get(id).toDict()
    return jsonify(response)


def create(item):
    model = SituacaoModel(item)

    db.session.add(model)
    db.session.commit()
    return model
