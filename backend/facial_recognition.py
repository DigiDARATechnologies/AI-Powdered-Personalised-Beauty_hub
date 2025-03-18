import cv2
import mediapipe as mp
import numpy as np
from deepface import DeepFace

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)
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
    except:
        return "Medium"