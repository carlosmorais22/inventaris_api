from flask import request, jsonify
from datetime import datetime

from ..app import db
from .models import Inventario

# ----------------------------------------------- #

# Query Object Methods => https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query
# Session Object Methods => https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522

def retrieve_controller(id):
    response = Inventario.query.get(id).toDict()
    return jsonify(response)

def list_controller():
    try:
        lista = Inventario.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    response = []
    for objeto in lista: response.append(objeto.toDict())
    return jsonify(response)

def create_controller():
    request_form = request.form.to_dict()

    plaqueta = True if request_form['plaqueta'].lower() == 'true' else False 
    tem_numero_serie = True if request_form['tem_numero_serie'].lower() == 'true' else False 

    curr_dt = datetime.now()
    id = int(round(curr_dt.timestamp()))
    new = Inventario(
                        id                  = id,
                        ano                 = request_form['ano'],
                        bem                 = request_form['bem'],
                        estado              = request_form['estado'],
                        situacao            = request_form['situacao'],
                        plaqueta            = plaqueta,
                        observacao          = request_form['observacao'],
                        cadastrado_por      = request_form['cadastrado_por'],
                        situacao_observacao = request_form['situacao_observacao'],
                        tem_numero_serie    = tem_numero_serie,
                        numero_serie        = request_form['numero_serie'],
                          )
    db.session.add(new)
    db.session.commit()

    response = Inventario.query.get(id).toDict()
    return jsonify(response)

