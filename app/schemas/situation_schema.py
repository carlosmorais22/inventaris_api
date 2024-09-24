from ..app import ma
from ..models.situation_model import SituationModel

from marshmallow import fields

class SituationSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = SituationModel
        load_instance = True
        include_fk = True

        descricao = fields.String()

