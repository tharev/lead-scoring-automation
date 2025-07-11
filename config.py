#!/usr/bin/env python3
"""
Configuration Management for AI-Powered Lead Scoring Automation System
Centralized configuration for database, ML models, APIs, and system settings.

Author: AI Sales Team
Version: 1.0.0
License: MIT
"""

import os
from datetime import timedelta
from typing import Dict, Any, Optional

class Config:
    """Base configuration class with common settings"""
    
    # Application Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lead-scoring-super-secret-key-change-in-production'
    DEBUG = False
    TESTING = False
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///lead_scoring.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
