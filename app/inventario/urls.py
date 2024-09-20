from flask import request

from ..app import app
from .controllers import list_controller, retrieve_controller, create_controller

@app.route("/inventario", methods=['GET', 'POST'])
def listInventario():
    if request.method == 'GET': 
        return list_controller()
    if request.method == 'POST': 
        return create_controller()
    else: 
        return 'Method is Not Allowed'

@app.route("/inventario/<id>", methods=['GET'])
def retrieveInventario(id):
    if request.method == 'GET': return retrieve_controller(id)
    else: return 'Method is Not Allowed'