import spacy
from flask import Blueprint, request, jsonify

chatbot_bp = Blueprint('chatbot', __name__)
nlp = spacy.load('en_core_web_sm')

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json.get('message')
    doc = nlp(message)
    if 'appointment' in message:
        response = "You can book an appointment online."
    elif 'service' in message:
        response = "We offer a variety of services including haircuts, makeup, and more."
    else:
        response = "I am sorry, I do not understand."
    return jsonify({'message': response})