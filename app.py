from flask import Flask, request, jsonify
from database.main import init_db, createClient

from database.models.client import ClientData

app = Flask(__name__)

@app.route('/createclient', methods=['POST'])
def postCreateNewClient():
    body = request.get_json()
    clientData = ClientData(body['name'], body['email'])
    init_db()
    client = createClient(clientData)
    return client.name

app.run(port=5000, host='localhost', debug=True)