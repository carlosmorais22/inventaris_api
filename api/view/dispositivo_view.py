from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_cors import CORS

from ..entities.dispositivo import Dispositivo
from ..services import dispositivo_service
from ..schemas.dispositivo_schema import DispositivoSchema

class ListarIncluirEditarDispositivo(Resource):
    def get(self):
        lista = dispositivo_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)

    def post(self):
        try:
            new = Dispositivo(
                            id         = request.json['id'],
                            nome       = request.json['nome'],
                            cpf        = request.json['cpf'],
                            modelo     = request.json['modelo'],
                            fabricante = request.json['fabricante'],
                            status     = request.json['status'],
                            is_adm     = request.json['is_adm'],
                            orgao      = 'UERR' if request.json['orgao'] != None else request.json['orgao'],
                        )
            
            resultado = dispositivo_service.create(new)
            schema = DispositivoSchema()
            return make_response(schema.jsonify(resultado), 200)


        except Exception as e:
            msg_error = f'Erro ao tentar incluir novo registro! \n{e}'
            print(msg_error)
            return make_response(jsonify(msg_error), 400,)
    
    def put(self):
        try:
            new = Dispositivo(
                            id         = request.json['id'],
                            nome       = request.json['nome'],
                            cpf        = request.json['cpf'],
                            modelo     = request.json['modelo'],
                            fabricante = request.json['fabricante'],
                            status     = request.json['status'],
                            is_adm     = request.json['is_adm'],
                            orgao      = 'UERR' if request.json['orgao'] != None else request.json['orgao'],
                        )
            
            resultado = dispositivo_service.update(new)
            schema = DispositivoSchema()
            return make_response(schema.jsonify(resultado), 200)


        except Exception as e:
            msg_error = f'Erro ao tentar incluir novo registro! \n{e}'
            print(msg_error)
            return make_response(jsonify(msg_error), 400,)

class RecuperarDispositivo(Resource):
    def get(self, id):
        item = dispositivo_service.recuperar(id)
        if item != None:
            return make_response(item, 201)
        return make_response({}, 201)

class RecuperarDispositivoV2(Resource):
    def get(self, id, modelo, fabricante):
        item = dispositivo_service.recuperarPorIdMotivoFabricante(id, modelo, fabricante)
        if item != None:
            return make_response(item, 201)
        return make_response({}, 201)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListarIncluirEditarDispositivo, '/api/dispositivo')
api.add_resource(RecuperarDispositivo, '/api/dispositivo/<string:id>')
api.add_resource(RecuperarDispositivoV2, '/api/dispositivo/<string:id>/<string:modelo>/<string:fabricante>')
