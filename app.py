from flask import Flask
from controller.client_controller import client_bp
from controller.boardgame_controller import boardgame_bp

app = Flask(__name__)

app.register_blueprint(client_bp, url_prefix="/client")
app.register_blueprint(boardgame_bp, url_prefix="/boardgame")

app.run(port=5000, host='localhost', debug=True)