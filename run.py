#!/usr/bin/env python3
"""
Main entry point for the ASL Detection System.
This script runs the application from the project root directory.
"""

import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Import and run the main application
from src.main import main

if __name__ == "__main__":
    main()
