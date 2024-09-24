from ..app import ma
from ..models.inventory_model import InventoryModel

from marshmallow import fields

class InventorySchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = InventoryModel
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
        created_at = fields.DateTime()
        updated_at = fields.DateTime()
        deleted_at = fields.DateTime()
