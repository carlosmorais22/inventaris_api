from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify
from flask_cors import CORS

from ..services import ano_service

class RecuperarAnoAtual(Resource):
    def get(self):
        ano = ano_service.recuperarAtual()
        return make_response(jsonify(ano.to_dict()), 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(RecuperarAnoAtual, '/api/ano')
