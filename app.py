from flask import Flask
from controller.client_controller import clientBluePrint

app = Flask(__name__)

app.register_blueprint(clientBluePrint, url_prefix="/client")

app.run(port=5000, host='localhost', debug=True)