from ..app import ma
from ..models.conta_model import ContaModel

from marshmallow import fields

class ContaSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = ContaModel
        load_instance = True
        include_fk = True

        descricao = fields.String()
        tem_numero_serie = fields()
        vida_util = fields.Integer()
        ativo = fields.Boolean()
