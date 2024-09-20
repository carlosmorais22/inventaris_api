from ..app import ma
from ..models.situacao_model import SituacaoModel

from marshmallow import fields

class SituacaoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = SituacaoModel
        load_instance = True
        include_fk = True

        descricao = fields.String()

