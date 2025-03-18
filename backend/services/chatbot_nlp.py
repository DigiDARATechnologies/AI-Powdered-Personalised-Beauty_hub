# backend/services/chatbot_nlp.py
import re
from datetime import datetime

class ChatbotNLP:
    def __init__(self):
        self.intents = {
            "greetings": ["hi", "hello", "hey", "greetings"],
            "farewells": ["bye", "goodbye", "see you", "cya"],
            "haircut": ["haircut", "hair style", "hair recommendation", "what haircut"],
            "makeup": ["makeup", "makeup style", "makeup recommendation", "what makeup"],
            "booking": ["book", "appointment", "schedule", "make an appointment"],
            "help": ["help", "assistance", "support", "what can you do"]
        }
        self.responses = {
            "greetings": ["Hello! How can I assist you with your beauty needs today?", "Hi there! What can I help you with?"],
            "farewells": ["Goodbye! Have a beautiful day!", "See you later! Take care!"],
            "help": ["I can help with haircuts, makeup recommendations, and booking appointments. What would you like to know?"],
            "default": ["Sorry, I didn’t understand that. Can you rephrase or ask about haircuts, makeup, or booking?"]
        }
        self.facial_data = None  # Store latest facial analysis for personalization

    def update_facial_data(self, facial_data):
        """Update chatbot with the latest facial analysis for personalized responses."""
        self.facial_data = facial_data

    def process_message(self, message):
        """Process user message and return a personalized, natural response."""
        message = message.lower().strip()
        
        # Greetings and farewells
        if any(greet in message for greet in self.intents["greetings"]):
            return self.responses["greetings"][0]
        if any(farewell in message for farewell in self.intents["farewells"]):
            return self.responses["farewells"][0]

        # Help intent
        if any(help_word in message for help_word in self.intents["help"]):
            return self.responses["help"][0]

        # Haircut recommendation (personalized)
        if any(haircut in message for haircut in self.intents["haircut"]):
            if self.facial_data and 'haircut' in self.facial_data:
                return f"Based on your latest analysis, I recommend a {self.facial_data['haircut']} haircut for your {self.facial_data['face_shape']} face shape."
            return "I recommend a Side Part haircut, but for a personalized suggestion, please analyze your face first!"

        # Makeup recommendation (personalized)
        if any(makeup in message for makeup in self.intents["makeup"]):
            if self.facial_data and 'makeup' in self.facial_data:
                return f"Based on your latest analysis, I suggest a {self.facial_data['makeup']} makeup style for your {self.facial_data['skin_tone']} skin tone."
            return "I recommend a Natural Glow makeup, but for a personalized suggestion, please analyze your face first!"

        # Booking intent (extract date and service if provided)
        if any(book in message for book in self.intents["booking"]):
            date_match = re.search(r'\d{4}-\d{2}-\d{2}', message)  # Simple date pattern (YYYY-MM-DD)
            service_match = re.search(r'(haircut|makeup)', message, re.IGNORECASE)
            date = date_match.group(0) if date_match else datetime.now().strftime('%Y-%m-%d')
            service = service_match.group(0) if service_match else "Haircut"
            return f"I've scheduled a {service} appointment for {date}. Would you like to confirm?"

        return self.responses["default"][0]

# Singleton instance for the chatbot
chatbot = ChatbotNLP()

def process_message(message):
    """Wrapper to process messages with the chatbot instance."""
    return chatbot.process_message(message)