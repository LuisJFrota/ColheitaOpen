from flask import Blueprint, request, jsonify 
from database.main import init_db
from services.client_services import create_client, edit_client, delete_client, get_all_clients

from database.models.client import ClientData

clientBluePrint = Blueprint('client', __name__)

@clientBluePrint.route('/list', methods=['GET'])
def getListClient():
    data = get_all_clients()

    result : ClientData = []
    for client in data:
        result.append({ 'id': client.id, 'name': client.name, 'email': client.email })
    return jsonify(result)
    

@clientBluePrint.route('/create', methods=['POST'])
def postCreateNewClient():
    body = request.get_json()

    clientData = ClientData(body['name'], body['email'])
    init_db()
    client = create_client(clientData)
    return client.name

@clientBluePrint.route('/edit/<int:id>', methods=['PUT'])
def putEditClient(id):
    body = request.get_json()

    clientData = ClientData(body['name'], body['email'])
    init_db()
    client = edit_client(id, clientData)
    return client.name

@clientBluePrint.route('/delete/<int:id>', methods=['DELETE'])
def deleteClientById(id):
    init_db()
    deleteResult = delete_client(id)
    return jsonify({'deleted': deleteResult})