from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify
from flask_cors import CORS

from ..schemas.situacao_schema import SituacaoSchema

from ..services import situacao_service

class ListAll(Resource):
    def get(self):
        lista = situacao_service.list()

        resultado = []
        # print(lista)

        for item in lista:
            print(item.to_dict())
            resultado.append(item.to_dict())
            
        #     resultado.append({
        #                     'id': item.id,
        #                     'descricao': item.descricao
        #             })


        # # schema = AtendimentoSchema(many=True)
        return make_response(jsonify(resultado), 201)
        # # return ""
        # schema = SituacaoSchema(many=True)
        # return make_response(jsonify(resultado), 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListAll, '/api/situacao')
