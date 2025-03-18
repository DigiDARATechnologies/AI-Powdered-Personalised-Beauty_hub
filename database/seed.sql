-- database/seed.sql
INSERT INTO facial_analysis (face_shape, skin_tone, haircut, makeup, eye_shape, lip_fullness, face_feature, eye_feature) VALUES
('Round', 'Warm', 'Side Part', 'Earthy Shades', 'Almond', 'Full', 'Soft Jawline', 'Upturned');

INSERT INTO history (appointment_date, service, status) VALUES
('2025-02-15 10:00:00', 'Haircut', 'Completed'),
('2025-02-18 14:00:00', 'Makeup', 'Pending');