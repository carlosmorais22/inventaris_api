from ..app import ma
from ..models.bem_model import BemModel

from marshmallow import fields

class BemSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = BemModel
        load_instance = True
        include_fk = True

        setor = fields.String()
        tombo = fields.String()
        descricao = fields.String()
        conta = fields.String()
        estado = fields.String()
        estado_descricao = fields.String()
        valor = fields.Numeric()
        valor_remanescente = fields.Numeric()
        numero_serie = fields.String()
        data = fields.DateTime()
        data_aquisicao = fields.DateTime()
        ativo = fields.Integer()
        inventariado = fields.Boolean()
