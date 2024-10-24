from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
import urllib.parse

from sqlalchemy import text

app = Flask(__name__) 

# string de conexão com o banco de dados
# host = 'testes.patrimonio.uerr.edu.br'
host = 'testes.patrimonio.uerr.edu.br'
usuario = 'sigpat'
senha = '@@sigp@t200'
database = 'sigpat'
# host = 'localhost'
# usuario = 'sigpat'
# usuario = 'postgres'
# senha = 'Admin'
urllib.parse.quote_plus(usuario)
urllib.parse.quote_plus(senha)

conexao_banco = "postgresql+psycopg2://{}:{}@{}/{}"
conexao_banco = conexao_banco.format(urllib.parse.quote_plus(usuario),urllib.parse.quote_plus(senha),host,database)
app.config['SQLALCHEMY_DATABASE_URI'] = conexao_banco # "postgresql+psycopg2://postgres:Admin@localhost/sigpat"

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

from .view import bem_view
from .view import conta_view
from .view import estado_view
from .view import inventario_view
from .view import situacao_view
from .view import ano_view
from .view import setor_view
from .view import dispositivo_view

def mac_from_ip(ip):
    arp_table = get_arp_table()

    for entry in arp_table:
        if entry['IP address'] == ip:
            return entry['HW address']
    return None

# Rota para teste de conexão
@app.route("/")
def hello():
    with db.session.connection() as connection:
        connection.execute(text('SET SESSION "app.user_name" = ''sigpat''').execution_options(autocommit=True))
        connection.execute(text('SET SESSION "app.ip_address" = ''ip_address''').execution_options(autocommit=True))
        connection.execute(text('SET SESSION "app.mac_address" = ''mac_address''').execution_options(autocommit=True))

        result = connection.execute(text("select current_setting('app.user_name') as col1, current_setting('app.ip_address') as col2, current_setting('app.mac_address') as col3").execution_options(autocommit=True))
        for r in result:
            print(r[0]) # Access by positional index
            print(r[1]) # Access by positional index
            print(r[2]) # Access by positional index
        result = connection.execute(text("update inventaris.teste set texto='321'").execution_options(autocommit=True))
        connection.commit()
        print("######################################")
        print(result)
        print("######################################")
        result = connection.execute(text("select current_setting('app.user_name') as col1, current_setting('app.ip_address') as col2, current_setting('app.mac_address') as col3").execution_options(autocommit=True))
        for r in result:
            print(r[0]) # Access by positional index
            print(r[1]) # Access by positional index
            print(r[2]) # Access by positional index
            return r[0]


    return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0')
