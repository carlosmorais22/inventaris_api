from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_cors import CORS

from ..schemas.situacao_schema import SituacaoSchema
from ..services import situacao_service
from ..entities.situacao import Situacao


class ListarSituacao(Resource):
    def get(self):
        lista = situacao_service.list()
        print(lista)

        resultado = []

        for item in lista:
            print(item)
            resultado.append(item.to_dict())
        return make_response(jsonify(resultado), 201)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListarSituacao, '/api/situacao')
