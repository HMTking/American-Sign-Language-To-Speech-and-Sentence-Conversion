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
├── app.py                        # Local dev entry point (python app.py)
├── wsgi.py                       # Production WSGI entry point (gunicorn wsgi:app)
├── asl_app/                      # Application package
│   ├── __init__.py               # create_app() application factory
│   ├── config.py                 # Environment-based configuration
│   ├── routes/                   # Flask blueprints (route layer)
│   │   ├── main.py               #   page route (/)
│   │   └── api.py                #   JSON API (/process_frame, /suggest, ...)
│   ├── services/                 # Business logic (framework-agnostic)
│   │   ├── classifier.py         #   GestureClassifier (TFLite inference)
│   │   ├── spelling.py           #   SpellingService (autocomplete + correction)
│   │   └── speech.py             #   gTTS text-to-speech
│   ├── models/keypoint_classifier/
│   │   ├── keypoint_classifier.tflite     # Trained TFLite model
│   │   └── keypoint_classifier_label.csv  # Gesture labels (A-Z)
│   └── templates/
│       └── index.html            # Web interface (camera UI)
├── tests/                        # Pytest smoke tests
├── requirements.txt              # Python dependencies
├── Procfile                      # Process command for deployment
├── render.yaml                   # Render Blueprint (one-click deploy)
├── USER_GUIDE.md                 # Sign + action reference
└── RENDER_DEPLOYMENT.md          # Deployment guide
```

### Architecture
The app uses the **Flask application-factory pattern** with a clean separation
of concerns:

- **`routes/`** — thin HTTP layer that parses requests and returns JSON.
- **`services/`** — reusable business logic (model inference, spelling, TTS)
  with no Flask dependency, instantiated once in `create_app` and shared via
  `app.extensions`.
- **`config.py`** — environment-specific settings selected by `FLASK_ENV`.

---

## 🚀 Quick Start

### 1. Create Virtual Environment (Recommended)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
# Local development
python app.py

# Production-style (WSGI)
gunicorn wsgi:app
```
Then open http://127.0.0.1:5000 in your browser and allow camera access.

### 4. Run the Tests (optional)
```bash
pip install pytest
pytest
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
| **Computer Vision** | OpenCV | Real-time hand region detection |
| **Machine Learning** | TFLite (LiteRT) | ASL gesture classification |
| **Audio Processing** | gTTS | Text-to-speech conversion |
| **Interface** | Flask + HTML/JS | Browser-based camera UI |

---

## 🎯 Usage Instructions

1. **Launch the application** using `python app.py`
2. **Open** http://127.0.0.1:5000 and allow camera access
3. **Make ASL gestures** - the system recognizes letters A-Z
4. **Form words** by spelling them out letter by letter
5. **Listen** as the system converts recognized text to speech

---

## 📊 Model Performance
- **Training Dataset**: 87,000+ ASL images + 10,000+ videos
- **Accuracy**: 95% on test data
- **Real-time Performance**: 30+ FPS on standard hardware
- **Supported Gestures**: All 26 ASL letters (A-Z)

---

## 🔧 Deployment

This app is ready to deploy on [Render](https://render.com). See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for a step-by-step guide, or use the included `render.yaml` Blueprint for one-click setup.

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
