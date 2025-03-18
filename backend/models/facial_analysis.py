# backend/models/facial_analysis.py
import mysql.connector
from config.db_config import db_config

def get_facial_analysis():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT face_shape, skin_tone, haircut, makeup, eye_shape, lip_fullness, face_feature, eye_feature FROM facial_analysis ORDER BY analyzed_at DESC LIMIT 1")
    data = cursor.fetchone()
    conn.close()
    return data

def save_facial_analysis(data):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO facial_analysis (face_shape, skin_tone, haircut, makeup, eye_shape, lip_fullness, face_feature, eye_feature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (data['face_shape'], data['skin_tone'], data['haircut'], data['makeup'], 
         data['eye_shape'], data['lip_fullness'], data['face_feature'], data['eye_feature'])
    )
    conn.commit()
    conn.close()