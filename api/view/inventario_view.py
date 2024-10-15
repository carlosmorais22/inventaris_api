from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_cors import CORS

from ..entities.inventario import Inventario
from ..services import inventario_service
from ..schemas.inventario_schema import InventarioSchema


class ListarIncluirInventario(Resource):
    def get(self):
        lista = inventario_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())

        return make_response(jsonify(resultado), 201)

    def post(self):
        try:
            new = Inventario(
                            ano                 = request.json['ano'],
                            bem                 = request.json['bem'],
                            estado              = request.json['estado'],
                            situacao            = request.json['situacao'],
                            plaqueta            = request.json['plaqueta'],
                            observacao          = request.json['observacao'],
                            cadastrado_por      = request.json['cadastrado_por'],
                            situacao_observacao = request.json['situacao_observacao'],
                            tem_numero_serie    = request.json['tem_numero_serie'],
                            numero_serie        = request.json['numero_serie'],
                            dispositivo         = request.json['dispositivo'],
                        )
            
            resultado = inventario_service.create(new)
            schema = InventarioSchema()
            return make_response(schema.jsonify(resultado), 200)


        except Exception as e:
            msg_error = f'Erro ao tentar incluir novo registro! \n{e}'
            print(msg_error)
            return make_response(jsonify(msg_error), 400,)

class RecuperarInventario(Resource):
    def get(self, setor, texto):
        lista = inventario_service.list()

        resultado = []

        print("#################################")

        for item in lista:
            print(item)
            resultado.append(item.to_dict())
        print("#################################")
            
        return make_response(jsonify(resultado), 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListarIncluirInventario, '/api/inventario')
api.add_resource(RecuperarInventario, '/api/inventario/<string:setor>/<string:texto>')
