from flask import Blueprint, request, jsonify
from database.main import init_db
from services.rent_services import (
    create_rent, 
    edit_rent, 
    delete_rent, 
    get_all_rents
)
from database.models.rent import RentData

rent_bp = Blueprint('rent', __name__)


@rent_bp.route('/list', methods=['GET'])
def get_list_rents():
    data = get_all_rents()

    result = []
    for rent in data:
        result.append({
            'id': rent.id,
            'date': rent.date,
            'totalCost': rent.totalCost,
            'client': rent.client
        })

    return jsonify(result)


@rent_bp.route('/create', methods=['POST'])
def post_create_rent():
    body = request.get_json()

    rent_data = RentData(
        date=body['date'],
        totalCost=body['totalCost'],
        client=body['client']
    )

    init_db()
    new_rent = create_rent(rent_data)

    return jsonify({
        'id': new_rent.id,
        'date': new_rent.date,
        'totalCost': new_rent.totalCost,
        'client': new_rent.client
    })


@rent_bp.route('/edit/<int:id>', methods=['PUT'])
def put_edit_rent(id):
    body = request.get_json()

    rent_data = RentData(
        date=body['date'],
        totalCost=body['totalCost'],
        client=body['client']
    )

    init_db()
    updated_rent = edit_rent(id, rent_data)

    return jsonify({
        'id': updated_rent.id,
        'date': updated_rent.date,
        'totalCost': updated_rent.totalCost,
        'client': updated_rent.client
    })


@rent_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_remove_rent(id):
    init_db()
    delete_result = delete_rent(id)
    return jsonify({'deleted': delete_result})
