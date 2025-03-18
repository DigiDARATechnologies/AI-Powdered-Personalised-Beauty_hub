# backend/app.py
from flask import Flask
from flask_cors import CORS
from routes.facial_routes import facial_bp
from routes.appointment_routes import appointment_bp
from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

app.register_blueprint(facial_bp, url_prefix='/api')
app.register_blueprint(appointment_bp, url_prefix='/api')
app.register_blueprint(chat_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)