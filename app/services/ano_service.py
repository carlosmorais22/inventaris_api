from flask import request, jsonify
import uuid

from ..app import db
from ..models.ano_model import AnoModel

def recuperarAtual():
    return AnoModel.query.filter_by(atual=True).first()
