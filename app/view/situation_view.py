from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_cors import CORS

from ..services import situation_service

class ListCreateSituations(Resource):
    def get(self):
        lista = situation_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListCreateSituations, '/api/situation')
