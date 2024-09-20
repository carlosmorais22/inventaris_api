from flask import request

from ..app import app
from .controllers import list_controller, retrieve_controller

@app.route("/conta", methods=['GET'])
def listConta():
    if request.method == 'GET': 
        return list_controller()
    else: 
        return 'Method is Not Allowed'

@app.route("/conta/<id>", methods=['GET'])
def retrieveConta(id):
    if request.method == 'GET': return retrieve_controller(id)
    else: return 'Method is Not Allowed'