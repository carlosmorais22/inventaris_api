from flask import request

from ..app import app
from .controllers import list_controller, retrieve_controller

@app.route("/estado", methods=['GET'])
def listEstado():
    if request.method == 'GET': 
        return list_controller()
    else: 
        return 'Method is Not Allowed'

@app.route("/estado/<id>", methods=['GET'])
def retrieveEstado(id):
    if request.method == 'GET': return retrieve_controller(id)
    else: return 'Method is Not Allowed'