from ..app import ma
from ..models.inventario_model import InventarioModel

from marshmallow import fields

class InventarioSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = InventarioModel
        load_instance = True
        include_fk = True

        ano = fields.Integer()
        bem = fields.Integer()
        estado = fields.Integer()
        situacao = fields.Integer()
        plaqueta = fields.Boolean()
        observacao = fields.String()
        cadastrado_por = fields.Integer()
        situacao_observacao = fields.String()
        tem_numero_serie = fields.Boolean()
        numero_serie = fields.String()
        dispositivo = fields.String()
        created_at = fields.DateTime()
        updated_at = fields.DateTime()
        deleted_at = fields.DateTime()
