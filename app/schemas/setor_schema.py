from ..app import ma
from ..models.setor_model import SetorModel

from marshmallow import fields

class SetorSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = SetorModel
        load_instance = True
        include_fk = True

        nome = fields.String()
        sigla = fields()
