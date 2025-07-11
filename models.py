"""
Database Models for AI-Powered Lead Scoring Automation System
============================================================

This module defines the SQLAlchemy database models for managing leads,
scoring algorithms, campaigns, and analytics in the lead scoring system.

Author: AI Lead Scoring Team
Version: 1.0.0
"""

from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json
from enum import Enum
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, JSON, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
import uuid

db = SQLAlchemy()

class LeadStatus(Enum):
    """Enumeration for lead status types"""
    NEW = "new"
