from ..app import ma
from ..models.dispositivo_model import DispositivoModel

from marshmallow import fields

class DispositivoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = DispositivoModel
        load_instance = True
        include_fk = True

        id = fields.String()
        nome = fields.String()
        cpf = fields.String()
        modelo = fields.String()
        fabricante = fields.String()
        status = fields.Boolean()
        is_adm = fields.Boolean()
        orgao = fields.String()
