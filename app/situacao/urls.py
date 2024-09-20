from flask import request

from ..app import app
from .controllers import list_controller, retrieve_controller

@app.route("/situacao", methods=['GET'])
def listSituacao():
    if request.method == 'GET': 
        return list_controller()
    else: 
        return 'Method is Not Allowed'

@app.route("/situacao/<id>", methods=['GET'])
def retrieveSituacao(id):
    if request.method == 'GET': return retrieve_controller(id)
    else: return 'Method is Not Allowed'