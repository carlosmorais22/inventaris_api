from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify
from flask_cors import CORS

from ..services import setor_service

class ListrSetor(Resource):
    def get(self):
        lista = setor_service.list()

        resultado = []

        for item in lista:
            print(item)
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListrSetor, '/api/setor')
