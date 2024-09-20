from flask import request, jsonify
import uuid

from ..app import db
from .models import Estado

# ----------------------------------------------- #

# Query Object Methods => https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query
# Session Object Methods => https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session
# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522

def list_controller():
    try:
        lista = Estado.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    response = []
    for objeto in lista: response.append(objeto.toDict())
    return jsonify(response)

def retrieve_controller(id):
    response = Estado.query.get(id).toDict()
    return jsonify(response)
