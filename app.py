from flask import Flask, request, jsonify
from database.main import init_db, createClient, getClient, editClient, deleteClient, getAllClient

from database.models.client import ClientData

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def getListClient():
    data = getAllClient()
    result : ClientData = []
    for client in data:
        result.append({ 'id': client.id, 'name': client.name, 'email': client.email })
    return jsonify(result)
    

@app.route('/createclient', methods=['POST'])
def postCreateNewClient():
    body = request.get_json()
    clientData = ClientData(body['name'], body['email'])
    init_db()
    client = createClient(clientData)
    return client.name

@app.route('/editclient/<int:id>', methods=['PUT'])
def putEditClient(id):
    body = request.get_json()
    clientData = ClientData(body['name'], body['email'])
    init_db()
    client = editClient(id, clientData)
    return client.name


app.run(port=5000, host='localhost', debug=True)