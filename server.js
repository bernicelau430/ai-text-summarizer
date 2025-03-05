const express = require('express');
const multer = require('multer');
const cors = require('cors');
const { spawn } = require('child_process');
const path = require('path');

const app = express();

// Configure multer for file upload
const storage = multer.diskStorage({
    destination: './uploads/',
    filename: function(req, file, cb) {
        cb(null, Date.now() + '-' + file.originalname);
    }
});

const upload = multer({ storage: storage });

app.use(cors());
app.use(express.static('./'));

// CHANGE PATH TO VENV BASED ON USER!!  
const PYTHON_PATH = '/Users/yiummy/ProgrammingStuff/VSCode/CSC480/torch_env/bin/python3'

// Serve the HTML file
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Handle file upload and process with Python
app.post('/upload', upload.single('file'), (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: 'No file uploaded' });
    }

    // Get the uploaded file path
    const filePath = path.join(__dirname, req.file.path);

    // Spawn Python process
    const pythonProcess = spawn(PYTHON_PATH, ['process_file.py', filePath]);

    let pythonData = "";

    // Collect data from Python script
    pythonProcess.stdout.on('data', (data) => {
        pythonData += data.toString();
    });

    // Handle Python script completion
    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: 'Python processing failed' });
        }
        
        //console.log('Response data:', { message: 'File uploaded and processed successfully', result: pythonData });
        res.json({ 
            message: 'File uploaded and processed successfully',
            result: pythonData
        });
    });

    // Handle Python errors
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python Error: ${data}`);
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});