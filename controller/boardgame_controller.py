from flask import Blueprint, request, jsonify 
from database.main import init_db
from services.boardgame_services import create_boardgame, edit_boardgame, delete_boardgame, get_all_boardgames

from database.models.boardgame import BoardGameData

boardgame_bp = Blueprint('boardgame', __name__)

@boardgame_bp.route('/list', methods=['GET'])
def get_list_boardgames():
    data = get_all_boardgames()

    result : BoardGameData = []
    for game in data:
        result.append({ 'id': game.id, 'boardGameName': game.boardGameName, 'cost': game.cost, 'playerCount': game.playerCount })
    return jsonify(result)
    

@boardgame_bp.route('/create', methods=['POST'])
def post_create_boardgame():
    body = request.get_json()

    gameData = BoardGameData(body['boardGameName'], body['cost'], body['playerCount'])
    init_db()
    game = create_boardgame(gameData)
    return game.boardGameName

@boardgame_bp.route('/edit/<int:id>', methods=['PUT'])
def put_edit_boardgame(id):
    body = request.get_json()

    clientData = BoardGameData(body['boardGameName'], body['cost'], body['playerCount'])
    init_db()
    game = edit_boardgame(id, clientData)
    return game.boardGameName

@boardgame_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_boardgame(id):
    init_db()
    deleteResult = delete_boardgame(id)
    return jsonify({'deleted': deleteResult})