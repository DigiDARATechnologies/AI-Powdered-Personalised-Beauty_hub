# AI-Powered Personalized Beauty Hub

Welcome to the **AI-Powered Personalized Beauty Hub**, a cutting-edge web application designed to revolutionize beauty parlour services. This project leverages artificial intelligence to provide personalized beauty recommendations (e.g., haircuts and makeup) based on facial analysis, integrates a responsive chatbot for customer support, and offers an online booking system. Built with a modern tech stack, it aims to enhance efficiency and user experience in the beauty industry.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Facial Recognition**: Analyzes uploaded or webcam-captured images to determine face shape, eye shape, lip fullness, skin tone, and provides personalized haircut and makeup recommendations.
- **Responsive Chatbot**: Offers natural language support for greetings, farewells, help, personalized beauty advice, and appointment scheduling with real-time updates.
- **Online Booking**: Allows users to book appointments for haircuts or makeup services with date flexibility.
- **User Dashboard**: Displays the latest facial analysis and booking history.
- **Cross-Platform Compatibility**: Fully responsive design for desktop, tablet, and mobile devices.
- **Secure and Anonymous**: Operates without requiring user authentication, ensuring privacy.

## Tech Stack
- **Frontend**:
  - React.js
  - HTML5, CSS3, JavaScript (ES6+)
- **Backend**:
  - Python (Flask)
  - Node.js (optional for scalability)
- **Database**:
  - MySQL
- **AI/ML**:
  - Facial recognition logic (custom implementation, expandable with OpenCV or TensorFlow)
- **Other Tools**:
  - npm for dependency management
  - ngrok for HTTPS testing
  - Git for version control

## Installation

### Prerequisites
- Node.js (v16 or later)
- Python (v3.8 or later)
- MySQL Server
- Git

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ai-powered-beauty-hub.git
   cd ai-powered-beauty-hub
   ```
2. **Set Up the Backend**
   Install Python dependencies
   ```sh
   cd backend
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```
   - Configure MySQL:
     - Create a database named beauty_hub
        ```sql
        CREATE DATABASE beauty_hub;
        ```
      - Update db_config in backend/models/db.py with your MySQL credentials:
        ```python
        db_config = {
            'user': 'your_username',
            'password': 'your_password',
            'host': 'localhost',
            'database': 'beauty_hub',
        }
      - Initialize the database with seed data:
        ```bash
        cd database
        Get-Content seed.sql | mysql -u your_username -p beauty_hub
        ```
    - Set Up the Frontend:
      - Install Node.js dependencies:
        ```base
        cd frontend
        npm install
        ```
      - Ensure logo.png is in public/ or import it from src/assets/ (see Logo Issue below).
    - Run the Application:
       - Start the backend
         ```sh
         cd backend
         .\venv\Scripts\activate
         python app.py
         ```
      - Start the frontend:
        ```sh
        cd frontend
        npm start
        ```
     - Open http://localhost:3000 in your browser

## Usage
- **Home Page**: Upload an image or use the webcam to analyze facial features and get personalized beauty recommendations.
- **Dashboard**: View your latest facial analysis and booking history.
- **Booking**: Schedule appointments for haircuts or makeup services.
- **Chatbot**: Interact with the AI chatbot for assistance, personalized advice, or booking requests (e.g., "Book a haircut for 2025-03-01").

## Project Structure
```bash
ai-powered-beauty-hub/
├── backend/                # Flask backend
│   ├── app.py             # Main application file
│   ├── routes/            # API route definitions
│   ├── models/            # Database models and queries
│   ├── services/          # Business logic (e.g., facial recognition, chatbot)
│   ├── uploads/           # Temporary image storage
│   └── requirements.txt   # Python dependencies
├── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # Reusable components (e.g., Navbar, Chatbot)
│   │   ├── pages/         # Page components (e.g., Home, Dashboard)
│   │   ├── assets/        # Static assets (e.g., logo.png, optional)
│   │   ├── styles/        # CSS files
│   │   └── App.js         # Main React app entry
│   ├── public/            # Static files (e.g., logo.png for public access)
│   └── package.json       # Node.js dependencies
├── database/              # SQL scripts
│   └── seed.sql           # Database initialization
├── README.md              # This file
└── LICENSE                # License file
```

## Configuration
- **Environment Variables**: Add a .env file in the backend/ directory for sensitive data (e.g., MySQL credentials) if needed.
- **CORS**: Ensure backend/app.py allows http://localhost:3000 (see flask_cors setup in code).
- **Webcam Permissions**: Grant camera access in your browser for facial recognition.

## API Endpoints
- *POST* /api/facial-analysis: Upload an image for facial analysis.
- *GET* /api/facial-analysis/latest: Retrieve the latest facial analysis.
- *GET* /api/history: Retrieve booking history (to be implemented).
- *POST* /api/chat: Interact with the chatbot.
- *POST* /api/appointment: Book an appointment (to be implemented).

## Contributing
 - Fork the repository.
 - Create a new branch (git checkout -b feature-branch).
 - Make your changes and commit them (git commit -m "Add feature").
 - Push to the branch (git push origin feature-branch).
 - Open a Pull Request with a detailed description of your changes.

## License
 - This project is licensed under the MIT License. See the LICENSE file for details.
