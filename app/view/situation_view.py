from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_cors import CORS

from ..schemas.situation_schema import SituationSchema
from ..services import situation_service
from ..entities.situation import Situation

class ListCreateSituations(Resource):
    def get(self):
        lista = situation_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)

    def post(self):
        try:
            new = Situation(
                            id        = 54,
                            descricao = request.json['descricao'],
                            status    = request.json['status'],
                        )
            resultado = situation_service.create(new)
            schema = SituationSchema()
            return make_response(schema.jsonify(resultado), 200)


        except Exception as e:
            msg_error = f'Erro ao tentar incluir novo registro! \n{e}'
            print(msg_error)
            return make_response(jsonify(msg_error), 400,)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListCreateSituations, '/api/situation')
