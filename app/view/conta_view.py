from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify
from flask_cors import CORS

from ..services import conta_service

class ListAllContas(Resource):
    def get(self):
        lista = conta_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListAllContas, '/api/conta')
