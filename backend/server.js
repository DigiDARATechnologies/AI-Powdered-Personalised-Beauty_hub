const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const { spawn } = require('child_process');
const multer = require('multer');
const path = require('path');

const app = express();
app.use(bodyParser.json());

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'beauty_hub',
});

db.connect(err => {
  if (err) throw err;
  console.log('MySQL Connected...');
});

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage: storage });

app.post('/appointments', (req, res) => {
  const { name, date, service } = req.body;
  const query = 'INSERT INTO appointments (name, date, service) VALUES (?, ?, ?)';
  db.query(query, [name, date, service], (err, result) => {
    if (err) throw err;
    res.send('Appointment booked successfully');
  });
});

app.post('/chat', (req, res) => {
  const { message } = req.body;
  const pythonProcess = spawn('python', ['chatbot.py', message]);

  pythonProcess.stdout.on('data', (data) => {
    res.json({ reply: data.toString() });
  });
});

app.post('/analyze-face', upload.single('image'), (req, res) => {
  const imagePath = req.file.path;
  const pythonProcess = spawn('python', ['facial_recognition.py', imagePath]);

  pythonProcess.stdout.on('data', (data) => {
    res.json({ result: data.toString() });
  });
});

app.listen(5000, () => {
  console.log('Server started on port 5000');
});