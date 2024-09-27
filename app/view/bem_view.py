from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify
from flask_cors import CORS

from ..services import bem_service

class ListBens(Resource):
    def get(self):
        lista = bem_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)
    
class RetrieveBens(Resource):
    def get(self, setor, texto):
        print(texto.upper())
        lista = bem_service.retrievePorSetor(texto.upper())

        resultado = []


        for item in lista:
            resultado.append(item.to_dict())
        print("#################################")
        print(len(resultado))
        print("#################################")
            
        return make_response(jsonify(resultado), 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListBens, '/api/bem')
api.add_resource(RetrieveBens, '/api/bem/<string:setor>/<string:texto>')
