# backend/routes/facial_routes.py
from flask import Blueprint, jsonify, request
from services.facial_recognition import analyze_face
from models.facial_analysis import save_facial_analysis, get_facial_analysis
import os
import logging

facial_bp = Blueprint('facial', __name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@facial_bp.route('/facial-analysis', methods=['POST'])
def facial_analysis():
    """
    Endpoint to analyze facial features from an uploaded image.
    Expects a file upload with key 'image'.
    """
    if 'image' not in request.files:
        logger.error("No image provided in request")
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    
    # Define upload folder relative to backend directory
    upload_folder = os.path.join(os.path.dirname(__file__), "uploads")
    os.makedirs(upload_folder, exist_ok=True)
    image_path = os.path.join(upload_folder, file.filename)
    
    try:
        logger.info(f"Saving image to {image_path}")
        file.save(image_path)
        if not os.path.exists(image_path):
            logger.error(f"Failed to save image at {image_path}")
            return jsonify({"error": "Failed to save image"}), 500

        logger.info(f"Analyzing image: {image_path}")
        analysis = analyze_face(image_path)
        if "error" in analysis:
            logger.error(f"Analysis failed: {analysis['error']}")
            return jsonify(analysis), 400

        logger.info(f"Saving analysis")
        save_facial_analysis(analysis)

        return jsonify({"message": "Analysis saved", "data": analysis}), 201

    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        return jsonify({"error": str(e)}), 500

    finally:
        # Safely remove file if it exists
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
                logger.info(f"Removed temporary file: {image_path}")
            except Exception as e:
                logger.warning(f"Failed to remove {image_path}: {str(e)}")

@facial_bp.route('/facial-analysis/latest', methods=['GET'])
def get_latest_facial_analysis():
    data = get_facial_analysis()
    if data:
        return jsonify({"data": data}), 200
    return jsonify({"error": "No analysis available"}), 404