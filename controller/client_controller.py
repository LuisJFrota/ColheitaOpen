from flask import Blueprint, request, jsonify 
from database.main import init_db
from services.client_services import (
    create_client, 
    edit_client, 
    delete_client, 
    get_all_clients
)

from database.models.client import ClientData

client_bp = Blueprint('client', __name__)

@client_bp.route('/list', methods=['GET'])
def get_list_clients():
    data = get_all_clients()

    result : ClientData = []
    for client in data:
        result.append({ 'id': client.id, 'name': client.name, 'email': client.email })
    return jsonify(result)
    

@client_bp.route('/create', methods=['POST'])
def post_create_client():
    body = request.get_json()

    clientData = ClientData(body['name'], body['email'])
    init_db()
    client = create_client(clientData)
    return client.name

@client_bp.route('/edit/<int:id>', methods=['PUT'])
def put_edit_client(id):
    body = request.get_json()

    clientData = ClientData(body['name'], body['email'])
    init_db()
    client = edit_client(id, clientData)
    return client.name

@client_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_remove_client(id):
    init_db()
    deleteResult = delete_client(id)
    return jsonify({'deleted': deleteResult})