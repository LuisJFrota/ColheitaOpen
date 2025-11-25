from flask import Flask
from controller.client_controller import client_bp
from controller.boardgame_controller import boardgame_bp
from controller.rent_boardgame_controller import rentboardgame_bp
from controller.rent_controller import rent_bp

app = Flask(__name__)

app.register_blueprint(client_bp, url_prefix="/client")
app.register_blueprint(boardgame_bp, url_prefix="/boardgame")
app.register_blueprint(rentboardgame_bp, url_prefix="/rentboardgame")
app.register_blueprint(rent_bp, url_prefix="/rent")

app.run(port=5000, host='localhost', debug=True)