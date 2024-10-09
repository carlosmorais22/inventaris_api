from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify
from flask_cors import CORS

from ..services import usuario_service

class ListarUsuario(Resource):
    def get(self):
        lista = usuario_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)
    
class RecuperarUsuario(Resource):
    def get(self, id):
        item = usuario_service.recuperar(id)
        if item != None:
            return make_response(item, 201)
        return make_response({}, 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListarUsuario, '/api/usuario')
api.add_resource(RecuperarUsuario, '/api/usuario/<string:id>')
