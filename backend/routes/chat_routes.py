# backend/routes/chat_routes.py
from flask import Blueprint, jsonify, request
from services.chatbot_nlp import chatbot, process_message
from models.facial_analysis import get_facial_analysis

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chatbot interactions.
    Expects a JSON payload with 'message' key.
    Returns a JSON response with the chatbot's reply.
    """
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "No message provided"}), 400
        
        user_message = data['message']
        
        # Update chatbot with latest facial analysis for personalization
        latest_analysis = get_facial_analysis()
        if latest_analysis:
            chatbot.update_facial_data(latest_analysis)

        reply = process_message(user_message)
        return jsonify({"reply": reply}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500