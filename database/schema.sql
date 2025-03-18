-- database/schema.sql
CREATE DATABASE IF NOT EXISTS beauty_hub;
USE beauty_hub;

DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS facial_analysis;

CREATE TABLE facial_analysis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    face_shape VARCHAR(50),
    skin_tone VARCHAR(50),
    haircut VARCHAR(100),
    makeup VARCHAR(100),
    eye_shape VARCHAR(50),
    lip_fullness VARCHAR(50),
    face_feature VARCHAR(100),
    eye_feature VARCHAR(100),
    analyzed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_date DATETIME,
    service VARCHAR(100),
    status ENUM('Completed', 'Pending', 'Cancelled') DEFAULT 'Pending'
);