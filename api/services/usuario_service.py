from flask import request, jsonify
import uuid

from ..app import db
from ..models.usuario_model import UsuarioModel
from ..entities.usuario import Usuario

def list():
    try:
        lista = UsuarioModel.query.all()
    except UnicodeDecodeError as e:
        return  f"Erro: {e}"
    except Exception as e:
        return  f"Erro: {e}"
    return lista

def recuperar(id):
    response = UsuarioModel.query.get(id)
    if (response != None):
        return response.to_dict()
    return None;


