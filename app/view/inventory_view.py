from ..app import app, api
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_cors import CORS
from datetime import datetime

from ..entities.inventory import Inventory
from ..services import inventory_service
from ..schemas.inventory_schema import InventorySchema

from sqlalchemy import Boolean
from sqlalchemy import TypeDecorator

class LiberalBoolean(TypeDecorator):
    impl = Boolean

    def process_bind_param(self, value):

        if value is not None:
            if isinstance(value, tuple):
                value = value[0]
            if isinstance(value,bool):
                return value
            value = bool(int(value))
        return value
    
class ListCreateInventorys(Resource):
    def get(self):
        lista = inventory_service.list()

        resultado = []

        for item in lista:
            resultado.append(item.to_dict())
            
        return make_response(jsonify(resultado), 201)

        
    def post(self):
        try:
            curr_dt = datetime.now()
            id = int(round(curr_dt.timestamp()))

            new = Inventory(
                            ano                 = request.json['ano'],
                            bem                 = request.json['bem'],
                            estado              = request.json['estado'],
                            situacao            = request.json['situacao'],
                            plaqueta            = 1,
                            observacao          = request.json['observacao'],
                            cadastrado_por      = request.json['cadastrado_por'],
                            situacao_observacao = request.json['situacao_observacao'],
                            tem_numero_serie    = 1,
                            numero_serie        = request.json['numero_serie'],
                        )
            
            resultado = inventory_service.create(new)
            schema = InventorySchema()
            return make_response(schema.jsonify(resultado), 200)


        except Exception as e:
            msg_error = f'Erro ao tentar incluir novo registro! \n{e}'
            print(msg_error)
            return make_response(jsonify(msg_error), 400,)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api.add_resource(ListCreateInventorys, '/api/inventory')
