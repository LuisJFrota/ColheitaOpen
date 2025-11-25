from flask import Blueprint, request, jsonify 
from database.main import init_db
from services.rentboardgame_services import (
    create_rentboardgame,
    edit_rentboardgame,
    delete_rentboardgame,
    get_all_rentboardgames
)
from database.models.rentboardgame import RentBoardGameData

boardgame_bp = Blueprint('rentboardgame', __name__)


@boardgame_bp.route('/list', methods=['GET'])
def get_list_rentboardgames():
    data = get_all_rentboardgames()

    result = []
    for item in data:
        result.append({
            'id': item.id,
            'rent': item.rent,
            'boardGame': item.boardGame,
            'quantity': item.quantity
        })

    return jsonify(result)


@boardgame_bp.route('/create', methods=['POST'])
def post_create_rentboardgame():
    body = request.get_json()

    rent_data = RentBoardGameData(
        rent=body['rent'],
        boardGame=body['boardGame'],
        quantity=body['quantity']
    )

    init_db()
    new_item = create_rentboardgame(rent_data)

    return jsonify({
        'id': new_item.id,
        'rent': new_item.rent,
        'boardGame': new_item.boardGame,
        'quantity': new_item.quantity
    })


@boardgame_bp.route('/edit/<int:id>', methods=['PUT'])
def put_edit_rentboardgame(id):
    body = request.get_json()

    rent_data = RentBoardGameData(
        rent=body['rent'],
        boardGame=body['boardGame'],
        quantity=body['quantity']
    )

    init_db()
    updated_item = edit_rentboardgame(id, rent_data)

    return jsonify({
        'id': updated_item.id,
        'rent': updated_item.rent,
        'boardGame': updated_item.boardGame,
        'quantity': updated_item.quantity
    })


@boardgame_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_remove_rentboardgame(id):
    init_db()
    result = delete_rentboardgame(id)
    return jsonify({'deleted': result})
