"""
Shared test fixtures for wayfinder-badge tests.

Provides TestClient fixture for testing FastAPI endpoints with proper state isolation.
"""

import pytest
from fastapi.testclient import TestClient
from src import app as app_module


@pytest.fixture
def client():
    """
    Provide a TestClient instance for testing FastAPI endpoints.
    
    Each test gets a fresh app instance with reset state to ensure test isolation.
    """
    # Reset the activities state for each test
    app_module.activities.clear()
    app_module.activities.update({
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Compete in basketball games and tournaments",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["james@mergington.edu", "marcus@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Develop tennis skills and compete in matches",
            "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["sarah@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and digital art techniques",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["lucy@mergington.edu", "alex@mergington.edu"]
        },
        "Music Band": {
            "description": "Play in the school band and perform at concerts",
            "schedule": "Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["noah@mergington.edu", "sophia@mergington.edu"]
        },
        "Robotics Club": {
            "description": "Build and program robots for competitions",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["ryan@mergington.edu", "jessica@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking and argumentation skills",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 14,
            "participants": ["thomas@mergington.edu", "emily@mergington.edu"]
        }
    })
    
    return TestClient(app_module.app)
