"""
Tests for the POST /activities/{activity_name}/signup endpoint.

Tests student signup functionality including happy path and error cases.
"""

import pytest


class TestSignup:
    """Tests for the POST /activities/{activity_name}/signup endpoint."""

    def test_signup_success(self, client):
        """
        Test successful signup for an activity.
        
        Arrange: Create test client with valid activity and email
        Act: POST /activities/{activity_name}/signup with valid data
        Assert: Verify 200 status and success message
        """
        # Arrange
        activity_name = "Chess Club"
        email = "newstudent@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 200
        assert f"Signed up {email} for {activity_name}" in response.json()["message"]

    def test_signup_adds_participant_to_activity(self, client):
        """
        Test that signup actually adds the participant to the activity.
        
        Arrange: Get initial activity data, prepare new student
        Act: POST signup request
        Assert: Verify participant appears in the activities list
        """
        # Arrange
        activity_name = "Tennis Club"
        email = "newtennis@mergington.edu"
        
        # Get initial participants count
        initial_response = client.get("/activities")
        initial_participants = initial_response.json()[activity_name]["participants"]
        initial_count = len(initial_participants)
        
        # Act
        signup_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Get updated activities
        updated_response = client.get("/activities")
        updated_participants = updated_response.json()[activity_name]["participants"]
        
        # Assert
        assert signup_response.status_code == 200
        assert len(updated_participants) == initial_count + 1
        assert email in updated_participants

    def test_signup_duplicate_email_returns_error(self, client):
        """
        Test that duplicate email signup returns 400 error.
        
        Arrange: Use an email already registered for the activity
        Act: POST signup with duplicate email
        Assert: Verify 400 status and error message
        """
        # Arrange
        activity_name = "Chess Club"
        duplicate_email = "michael@mergington.edu"  # Already in Chess Club
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": duplicate_email}
        )
        
        # Assert
        assert response.status_code == 400
        assert "already signed up" in response.json()["detail"].lower()

    def test_signup_nonexistent_activity_returns_error(self, client):
        """
        Test that signup to a nonexistent activity returns 404 error.
        
        Arrange: Prepare request with invalid activity name
        Act: POST signup with nonexistent activity
        Assert: Verify 404 status and error message
        """
        # Arrange
        activity_name = "Nonexistent Activity"
        email = "student@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 404
        assert "Activity not found" in response.json()["detail"]

    def test_signup_response_message_format(self, client):
        """
        Test that signup success response has the correct message format.
        
        Arrange: Create test client with valid data
        Act: POST signup request
        Assert: Verify response message includes both email and activity name
        """
        # Arrange
        activity_name = "Art Studio"
        email = "artlover@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        data = response.json()
        
        # Assert
        assert response.status_code == 200
        assert email in data["message"]
        assert activity_name in data["message"]
