# American Sign Language (ASL) Detection System

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.0+-orange?logo=tensorflow" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/Accuracy-95%25-brightgreen" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"/>
</div>

## 📌 Project Overview
This project, developed by **Datt Patel** from the **Indian Institute of Information Technology, Surat (IIIT Surat)**, is an AI-powered system that converts **American Sign Language (ASL) gestures into text and speech** in real time. It enables seamless communication for the deaf and hard-of-hearing community by bridging the gap between sign language and spoken language.

## 📁 Project Structure

```
American-Sign-Language-To-Speech-and-Sentence-Conversion/
├── src/                          # 🔹 IMPORTANT: Core application files
│   ├── main.py                   # Main application entry point
│   ├── model/                    # Pre-trained ML models
│   │   └── keypoint_classifier/
│   │       ├── keypoint_classifier.py
│   │       ├── keypoint_classifier.keras
│   │       ├── keypoint_classifier.tflite
│   │       ├── keypoint_classifier_label.csv
│   │       └── keypoint.csv
│   └── utils/                    # Utility modules
│       └── cvfpscalc.py
├── requirements.txt              # 🔹 IMPORTANT: Python dependencies
├── run.py                        # 🔹 IMPORTANT: Application launcher
├── docs/                         # 📖 Documentation files
│   └── README.md                 # Project documentation
└── development/                  # 🔧 Development files
    └── keypoint_classification.ipynb  # Model training notebook
```

### Important Files (Required for Running)
- `src/main.py` - Main application code
- `src/model/` - Pre-trained models and labels
- `src/utils/` - Utility functions
- `requirements.txt` - Python dependencies
- `run.py` - Application launcher

### Non-Critical Files
- `docs/README.md` - Documentation
- `development/keypoint_classification.ipynb` - Model training/development notebook

---

## 🚀 Quick Start

### 1. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv asl_env

# Activate virtual environment
# On Linux/Mac:
source asl_env/bin/activate
# On Windows:
# asl_env\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python run.py
```

### Alternative: Run from source directory
```bash
cd src
python main.py
```

### 4. Deactivate Virtual Environment (when done)
```bash
deactivate
```

### 🔧 Quick Environment Setup (Alternative)
```bash
# Make activation script executable and run it
chmod +x activate_env.sh
source activate_env.sh
```

---

## 🛠 How It Works
The system follows a structured pipeline to recognize and translate ASL gestures:

### <img src="https://img.icons8.com/color/24/000000/hand.png"/> Hand Detection & Tracking
- Uses **MediaPipe** to detect and track **21 hand landmarks** (key points) in real time
- Works efficiently even in **low-light conditions**

###  Feature Extraction
- Extracts **x and y coordinates** of the 21 landmarks (total **42 features**) from each video frame

### <img src="https://img.icons8.com/color/24/000000/artificial-intelligence.png"/> Gesture Classification
- A **Multi-Layer Perceptron (MLP)** neural network classifies hand poses into **ASL letters (A-Z)**
- Trained on **87,000+ ASL images** and **10,000+ finger-spelling videos** for high accuracy

###  Sentence Formation
- Recognized letters are combined into **words and full sentences** using NLP

###  Speech Conversion
- **Google Text-to-Speech (gTTS)** converts text into **natural-sounding speech**

---

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| ✅ **Real-time Recognition** | 95% accurate gesture detection |
| ✅ **Sentence Translation** | Interprets full ASL sentences |
| ✅ **Robust Performance** | Works in varying lighting conditions |
| ✅ **Instant Speech** | Low-latency audio feedback |

---

## 🖥 Technology Stack
<div align="center">
  <img src="https://img.shields.io/badge/OpenCV-5.0+-green?logo=opencv" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/MediaPipe-0.8.9-blue" alt="MediaPipe"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.10+-orange?logo=tensorflow" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/gTTS-2.2.4-green" alt="gTTS"/>
</div>

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Computer Vision** | OpenCV + MediaPipe | Real-time hand detection |
| **Machine Learning** | TensorFlow/Keras | ASL gesture classification |
| **Audio Processing** | gTTS + Pygame | Text-to-speech conversion |
| **Interface** | OpenCV GUI | Real-time video display |

---

## 🎯 Usage Instructions

1. **Launch the application** using `python run.py`
2. **Position your hand** in front of the camera
3. **Make ASL gestures** - the system will recognize letters A-Z
4. **Form words** by spelling them out letter by letter
5. **Listen** as the system converts recognized text to speech

### Controls:
- **ESC**: Exit the application
- **Space**: Clear current sentence
- **Enter**: Speak current sentence

---

## 📊 Model Performance
- **Training Dataset**: 87,000+ ASL images + 10,000+ videos
- **Accuracy**: 95% on test data
- **Real-time Performance**: 30+ FPS on standard hardware
- **Supported Gestures**: All 26 ASL letters (A-Z)

---

## 🔧 Development

For model training and development work, see the Jupyter notebook in the `development/` directory:
```bash
jupyter notebook development/keypoint_classification.ipynb
```

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

---

## 📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
**Datt Patel**  
Indian Institute of Information Technology, Surat (IIIT Surat)

---

<div align="center">
  <strong>Bridging the gap between sign language and spoken communication through AI 🤟</strong>
</div>
