from flask import request

from ..app import app
from .controllers import list_controller, retrieve_controller

@app.route("/bem", methods=['GET'])
def listBem():
    if request.method == 'GET': 
        return list_controller()
    else: 
        return 'Method is Not Allowed'

@app.route("/bem/<id>", methods=['GET'])
def retrieveBem(id):
    if request.method == 'GET': return retrieve_controller(id)
    else: return 'Method is Not Allowed'