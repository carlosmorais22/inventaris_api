from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__) 

# string de conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Admin@localhost/sigpat'

# Evita warnings desnecessários
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

ma = Marshmallow(app)

api = Api(app)    # app.run(host='0.0.0.0', port=5001)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def _repr_(self):
        return f'<Usuario {self.nome}>'

# from .accounts.urls import *
# from .situacao.urls import *
# from .bem.urls import *
# from .conta.urls import *
# from .estado.urls import *
# from .inventario.urls import *

from .view import situacao_view

# Rota para teste de conexão
@app.route('/')
def index():
    return 'Conectado!'

if __name__ == '_main_':
    app.run(host="0.0.0.0",debug=True)