# backend/services/facial_recognition.py
import cv2
import mediapipe as mp
import numpy as np
from deepface import DeepFace
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.3)
mp_drawing = mp.solutions.drawing_utils

def analyze_face_shape(landmarks, image_shape):
    jaw = [np.array(landmarks[i]) for i in [365, 397, 288, 435, 367, 364, 394, 395, 379]]
    jaw_width = np.linalg.norm(jaw[0] - jaw[-1])
    face_height = np.linalg.norm(np.array(landmarks[10]) - np.array(landmarks[152]))
    
    cheek_left = np.array(landmarks[123])
    cheek_right = np.array(landmarks[352])
    cheek_width = np.linalg.norm(cheek_left - cheek_right)
    
    ratio = jaw_width / face_height
    if ratio > 1.15:
        return "Square", "Prominent Jawline"
    elif ratio < 0.85:
        return "Round", "Soft Jawline"
    elif cheek_width / jaw_width > 0.95:
        return "Heart", "High Cheekbones"
    else:
        return "Oval", "Balanced Features"

def analyze_eye_shape(landmarks):
    left_eye = [landmarks[i] for i in [33, 160, 158, 133, 153, 144]]
    eye_width = np.linalg.norm(np.array(left_eye[3]) - np.array(left_eye[0]))
    eye_height = np.linalg.norm(np.array(left_eye[5]) - np.array(left_eye[1]))
    aspect_ratio = eye_height / eye_width
    
    if aspect_ratio > 0.3:
        return "Almond", "Upturned"
    elif aspect_ratio < 0.25:
        return "Round", "Downturned"
    else:
        return "Hooded", "Deep Set"

def analyze_lip_fullness(landmarks):
    upper_lip = np.linalg.norm(np.array(landmarks[13]) - np.array(landmarks[14]))
    lower_lip = np.linalg.norm(np.array(landmarks[17]) - np.array(landmarks[18]))
    total = upper_lip + lower_lip
    return "Full" if total > 0.15 else "Thin"

def analyze_skin_tone(image):
    try:
        analysis = DeepFace.analyze(img_path=image, actions=['race'], enforce_detection=False)
        dominant_race = analysis[0]['dominant_race']
        skin_tone_map = {
            'white': 'Fair', 
            'middle eastern': 'Olive',
            'asian': 'Golden',
            'indian': 'Warm',
            'latino hispanic': 'Medium',
            'black': 'Deep'
        }
        return skin_tone_map.get(dominant_race, 'Medium')
    except Exception as e:
        logger.error(f"Error in skin tone analysis: {str(e)}")
        return "Medium"

def analyze_face(image_path):
    """
    Analyze facial features from an image file path.
    Returns a dict with face shape, eye shape, lip fullness, and skin tone.
    """
    logger.info(f"Starting analysis for image: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        logger.error(f"Invalid image: {image_path}")
        return {"error": "Invalid image"}

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image_rgb)

    if not results.multi_face_landmarks:
        logger.error(f"No face detected in {image_path}")
        return {"error": "No face detected"}

    landmarks = results.multi_face_landmarks[0].landmark
    h, w, _ = image.shape
    normalized_landmarks = [(lm.x * w, lm.y * h) for lm in landmarks]

    face_shape, face_feature = analyze_face_shape(normalized_landmarks, image.shape)
    eye_shape, eye_feature = analyze_eye_shape(normalized_landmarks)
    lip_fullness = analyze_lip_fullness(normalized_landmarks)
    skin_tone = analyze_skin_tone(image_path)

    haircut_map = {
        "Square": "Textured Crop",
        "Round": "Side Part",
        "Heart": "Pompadour",
        "Oval": "Pixie Cut"
    }
    makeup_map = {
        "Fair": "Soft Pink",
        "Olive": "Bronze Glow",
        "Golden": "Peach Tones",
        "Warm": "Earthy Shades",
        "Medium": "Natural Glow",
        "Deep": "Bold Reds"
    }

    result = {
        "face_shape": face_shape,
        "face_feature": face_feature,
        "eye_shape": eye_shape,
        "eye_feature": eye_feature,
        "lip_fullness": lip_fullness,
        "skin_tone": skin_tone,
        "haircut": haircut_map.get(face_shape, "Pixie Cut"),
        "makeup": makeup_map.get(skin_tone, "Natural Glow")
    }
    logger.info(f"Analysis completed: {result}")
    return result