# ASL Web Application - Render Deployment Guide

## 🚀 Deploy Your ASL App on Render

### Prerequisites

- GitHub account with your code pushed
- Render account (free tier available)

### Step-by-Step Deployment:

#### 1. Prepare Your Repository

```bash
# Make sure these files are in your repo:
# - app.py (Flask web application)
# - requirements.txt (web dependencies)
# - Procfile (Render startup command)
# - render.yaml (Render Blueprint, optional)
# - templates/index.html (web interface)
# - src/model/ folder with your trained model
```

#### 2. Deploy on Render

1. Go to https://render.com and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure deployment:
   - **Name**: `asl-detection-app`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`

> Tip: Instead of configuring manually, you can choose **New + → Blueprint** and let Render read `render.yaml` automatically.

#### 3. Environment Variables

Set these in Render dashboard:

- `FLASK_ENV=production`
- `SECRET_KEY=your-random-secret-key-here`

#### 4. Access Your App

- Render will provide a URL like: `https://your-app-name.onrender.com`
- Users can access via web browser on any device with camera

### 🌟 Features of Web Version:

- ✅ **Browser-based** - No installation required
- ✅ **Mobile friendly** - Works on phones/tablets
- ✅ **Real-time detection** - Camera access via WebRTC
- ✅ **Cloud hosted** - Accessible anywhere
- ✅ **Auto-scaling** - Handles multiple users

### 🔧 Key Changes Made:

1. **Removed desktop dependencies** - No more cv.imshow(), camera hardware access
2. **Added web interface** - HTML/CSS/JavaScript frontend
3. **WebRTC integration** - Browser camera access
4. **REST API endpoints** - Process frames and generate speech
5. **Cloud-ready** - Uses headless OpenCV, production WSGI server

### 📱 How Users Will Use It:

1. Visit your Render URL
2. Allow camera access
3. Make ASL gestures in front of camera
4. See real-time recognition
5. Listen to generated speech
6. Share the URL with anyone!

### 💰 Cost:

- **Free tier**: 750 hours/month (plenty for testing)
- **Paid tier**: ~$7/month for always-on service

This solution makes your ASL app accessible to anyone with a web browser and camera! 🎉
