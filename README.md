American Sign Language (ASL) Detection System
Project Overview
This project, developed by Datt Patel from the Indian Institute of Information Technology, Surat (IIIT Surat), is an AI-powered system that converts American Sign Language (ASL) gestures into text and speech in real time. It enables seamless communication for the deaf and hard-of-hearing community by bridging the gap between sign language and spoken language.

How It Works
The system follows a structured pipeline to recognize and translate ASL gestures:

Hand Detection & Tracking

Uses MediaPipe to detect and track 21 hand landmarks (key points) in real time.

Works efficiently even in low-light conditions.

Feature Extraction

Extracts x and y coordinates of the 21 landmarks (total 42 features) from each video frame.

Gesture Classification

A Multi-Layer Perceptron (MLP) neural network classifies hand poses into ASL letters (A-Z).

The model was trained on 87,000+ ASL images and 10,000+ finger-spelling videos for high accuracy.

Sentence Formation

Recognized letters are combined into words and full sentences using natural language processing (NLP).

Speech Conversion

Google Text-to-Speech (gTTS) converts the translated text into natural-sounding speech instantly.

Key Features
 Real-time ASL Recognition – Detects and translates gestures with 95% accuracy.
 Sentence-Level Translation – Goes beyond single letters to interpret full ASL sentences.
 Robust Performance – Works in varying lighting and background conditions.
 Instant Speech Output – Provides low-latency audio feedback for smooth communication.

Technology Stack
🔹 Computer Vision – OpenCV, MediaPipe (for hand tracking)
🔹 Machine Learning – TensorFlow, Scikit-learn (MLP model training)
🔹 Natural Language Processing (NLP) – For sentence formation
🔹 Text-to-Speech (TTS) – gTTS (Google’s TTS engine)
🔹 Data Processing – NumPy, Pandas

Future Enhancements
🔸 Bidirectional Translation – Adding speech-to-ASL for two-way communication.
🔸 Support for Regional Sign Languages – Expanding beyond ASL to other sign languages.
🔸 Improved Temporal Modeling – Using LSTMs to better understand continuous signing.
🔸 Expanded Vocabulary – Adding more words, phrases, and contextual gestures.

