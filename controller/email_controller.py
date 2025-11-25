from flask import Blueprint, request, jsonify 
from database.main import init_db
from services.email_services import send_email

email_bp = Blueprint('email', __name__)

@email_bp.route('/send', methods=['POST'])
def post_send_email():
    body = request.get_json()
    to = body['to']
    subject = body['subject']
    message = body['message']

    send_email(to, subject, message)

    return jsonify({'status': 'Email sent successfully'})
