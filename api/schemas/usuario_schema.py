from ..app import ma
from ..models.usuario_model import UsuarioModel

from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = UsuarioModel
        load_instance = True
        include_fk = True

        id = fields.String()
        nome = fields.String()
        cpf = fields.String()
        modelo = fields.String()
        fabricante = fields.String()
        status = fields.Boolean()
