from ..app import ma
from ..models.ano_model import AnoModel

from marshmallow import fields

class AnoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = AnoModel
        load_instance = True
        include_fk = True

        atual = fields.Bool()
