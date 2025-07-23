#!/bin/bash
# Activation script for ASL project virtual environment

echo "🚀 Activating ASL Detection System virtual environment..."
source asl_env/bin/activate

echo "✅ Virtual environment activated!"
echo "📦 Installed packages:"
pip list --format=columns | head -10
echo "..."
echo ""
echo "🎯 To run the ASL application:"
echo "   python run.py"
echo ""
echo "🔄 To deactivate when done:"
echo "   deactivate"
echo ""
