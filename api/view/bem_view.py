from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify
from flask_cors import CORS

from ..services import bem_service

class ListarBem(Resource):
    def get(self):
        lista = bem_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)
    
class RecuperarBem(Resource):
    def get(self, tipo, texto):
        lista = []
        if tipo=="setor":
            lista = bem_service.recuperarPorSetor(texto.upper())
        if tipo=="tombo":
            lista = bem_service.recuperarPorTombo(texto.upper())
        if tipo=="descricao":
            lista = bem_service.recuperarPorDescricao(texto.upper())

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)

class RecuperarBemV2(Resource):
    def get(self, orgao, tipo, texto):
        lista = []
        if tipo=="setor":
            lista = bem_service.recuperarPorSetor(texto.upper(), orgao)
        if tipo=="tombo":
            lista = bem_service.recuperarPorTombo(texto.upper(), orgao)
        if tipo=="descricao":
            lista = bem_service.recuperarPorDescricao(texto.upper(), orgao)

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListarBem, '/api/bem')
api.add_resource(RecuperarBem, '/api/bem/<string:tipo>/<string:texto>')
api.add_resource(RecuperarBemV2, '/api/bem/<string:orgao>/<string:tipo>/<string:texto>')
