from ..app import ma
from ..models.estado_model import EstadoModel

from marshmallow import fields

class EstadoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = EstadoModel
        load_instance = True
        include_fk = True

        descricao = fields.String()
