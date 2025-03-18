# backend/models/history.py
import mysql.connector
from config.db_config import db_config

def get_history():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT appointment_date, service, status FROM history ORDER BY appointment_date DESC LIMIT 5")
    history = cursor.fetchall()
    conn.close()
    return history

def add_appointment(appointment_date, service):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO history (appointment_date, service) VALUES (%s, %s)",
        (appointment_date, service)
    )
    conn.commit()
    conn.close()