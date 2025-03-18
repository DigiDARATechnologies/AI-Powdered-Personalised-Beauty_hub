# backend/routes/appointment_routes.py
from flask import Blueprint, jsonify, request
from models.history import add_appointment, get_history

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/appointment', methods=['POST'])
def book_appointment():
    data = request.json
    appointment_date = data['appointment_date']
    service = data['service']
    add_appointment(appointment_date, service)
    return jsonify({"message": "Appointment booked"}), 201

@appointment_bp.route('/history', methods=['GET'])
def get_appointment_history():
    history = get_history()
    return jsonify({"history": history})