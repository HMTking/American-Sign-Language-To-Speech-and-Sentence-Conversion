# <img src="https://img.icons8.com/color/48/000000/sign-language.png" alt="ASL Icon"/> American Sign Language (ASL) Detection System

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.0+-orange?logo=tensorflow" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/Accuracy-95%25-brightgreen" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"/>
</div>

## 📌 Project Overview
This project, developed by **Datt Patel** from the **Indian Institute of Information Technology, Surat (IIIT Surat)**, is an AI-powered system that converts **American Sign Language (ASL) gestures into text and speech** in real time. It enables seamless communication for the deaf and hard-of-hearing community by bridging the gap between sign language and spoken language.

---

## 🛠 How It Works
The system follows a structured pipeline to recognize and translate ASL gestures:

### <img src="https://img.icons8.com/color/24/000000/hand.png"/> Hand Detection & Tracking
- Uses **MediaPipe** to detect and track **21 hand landmarks** (key points) in real time
- Works efficiently even in **low-light conditions**

### <img src="https://img.icons8.com/color/24/000000/feature.png"/> Feature Extraction
- Extracts **x and y coordinates** of the 21 landmarks (total **42 features**) from each video frame

### <img src="https://img.icons8.com/color/24/000000/artificial-intelligence.png"/> Gesture Classification
- A **Multi-Layer Perceptron (MLP)** neural network classifies hand poses into **ASL letters (A-Z)**
- Trained on **87,000+ ASL images** and **10,000+ finger-spelling videos** for high accuracy

### <img src="https://img.icons8.com/color/24/000000/speech-to-text.png"/> Sentence Formation
- Recognized letters are combined into **words and full sentences** using NLP

### <img src="https://img.icons8.com/color/24/000000/voice.png"/> Speech Conversion
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
  <img src="https://img.shields.io/badge/TensorFlow-2.7.0-orange?logo=tensorflow" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/gTTS-2.2.4-red" alt="gTTS"/>
  <img src="https://img.shields.io/badge/NumPy-1.21-blue" alt="NumPy"/>
</div>

---

## 🚀 Future Enhancements
- <img src="https://img.icons8.com/color/14/000000/communication.png"/> **Bidirectional Translation** (Speech-to-ASL)
- <img src="https://img.icons8.com/color/14/000000/globe.png"/> **Regional Sign Language Support**
- <img src="https://img.icons8.com/color/14/000000/neural-network.png"/> **LSTM-based Temporal Modeling**
- <img src="https://img.icons8.com/color/14/000000/dictionary.png"/> **Expanded Vocabulary**

---

<div align="center">
  <h3>📜 Acknowledgments</h3>
  <p>Special thanks to the faculty of <b>IIIT Surat</b> for their guidance and support.</p>
</div>
