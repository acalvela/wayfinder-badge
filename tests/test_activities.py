"""
Tests for the GET /activities endpoint.

Tests retrieving the list of activities and their structure.
"""

import pytest


class TestActivities:
    """Tests for the GET /activities endpoint."""

    def test_get_activities_returns_all_activities(self, client):
        """
        Test that GET /activities returns all 9 activities.
        
        Arrange: Create test client
        Act: GET /activities
        Assert: Verify 200 status and all 9 activities are returned
        """
        # Arrange
        # client fixture is injected via pytest
        expected_activities = [
            "Chess Club",
            "Programming Class",
            "Gym Class",
            "Basketball Team",
            "Tennis Club",
            "Art Studio",
            "Music Band",
            "Robotics Club",
            "Debate Team",
        ]
        
        # Act
        response = client.get("/activities")
        data = response.json()
        
        # Assert
        assert response.status_code == 200
        assert len(data) == 9
        assert list(data.keys()) == expected_activities

    def test_activities_have_correct_structure(self, client):
        """
        Test that each activity has the required fields.
        
        Arrange: Create test client
        Act: GET /activities
        Assert: Verify each activity has description, schedule, max_participants, and participants
        """
        # Arrange
        required_fields = {"description", "schedule", "max_participants", "participants"}
        
        # Act
        response = client.get("/activities")
        data = response.json()
        
        # Assert
        assert response.status_code == 200
        for activity_name, activity_data in data.items():
            assert set(activity_data.keys()) == required_fields
            assert isinstance(activity_data["description"], str)
            assert isinstance(activity_data["schedule"], str)
            assert isinstance(activity_data["max_participants"], int)
            assert isinstance(activity_data["participants"], list)

    def test_activities_have_participants(self, client):
        """
        Test that activities have the expected participants.
        
        Arrange: Create test client
        Act: GET /activities
        Assert: Verify Chess Club has michael and daniel, Programming Class has emma and sophia, etc.
        """
        # Arrange
        expected_participants = {
            "Chess Club": ["michael@mergington.edu", "daniel@mergington.edu"],
            "Programming Class": ["emma@mergington.edu", "sophia@mergington.edu"],
            "Gym Class": ["john@mergington.edu", "olivia@mergington.edu"],
        }
        
        # Act
        response = client.get("/activities")
        data = response.json()
        
        # Assert
        assert response.status_code == 200
        for activity_name, expected_emails in expected_participants.items():
            assert data[activity_name]["participants"] == expected_emails
