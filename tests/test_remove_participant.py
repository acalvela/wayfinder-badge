"""
Tests for the DELETE /activities/{activity_name}/participants/{email} endpoint.

Tests removing participants from activities including happy path and error cases.
"""

import pytest


class TestRemoveParticipant:
    """Tests for the DELETE /activities/{activity_name}/participants/{email} endpoint."""

    def test_remove_participant_success(self, client):
        """
        Test successful removal of a participant from an activity.
        
        Arrange: Create test client with existing participant
        Act: DELETE /activities/{activity_name}/participants/{email}
        Assert: Verify 200 status and success message
        """
        # Arrange
        activity_name = "Chess Club"
        email = "michael@mergington.edu"  # Existing participant
        
        # Act
        response = client.delete(f"/activities/{activity_name}/participants/{email}")
        
        # Assert
        assert response.status_code == 200
        assert f"Removed {email} from {activity_name}" in response.json()["message"]

    def test_remove_participant_removes_from_activity(self, client):
        """
        Test that removing a participant actually removes them from the activity.
        
        Arrange: Get initial participant list
        Act: DELETE request to remove participant
        Assert: Verify participant no longer in activity list
        """
        # Arrange
        activity_name = "Programming Class"
        email = "emma@mergington.edu"  # Existing participant
        
        # Get initial participants
        initial_response = client.get("/activities")
        initial_participants = initial_response.json()[activity_name]["participants"]
        initial_count = len(initial_participants)
        
        # Act
        delete_response = client.delete(f"/activities/{activity_name}/participants/{email}")
        
        # Get updated activities
        updated_response = client.get("/activities")
        updated_participants = updated_response.json()[activity_name]["participants"]
        
        # Assert
        assert delete_response.status_code == 200
        assert len(updated_participants) == initial_count - 1
        assert email not in updated_participants

    def test_remove_nonexistent_participant_returns_error(self, client):
        """
        Test that removing a nonexistent participant returns 404 error.
        
        Arrange: Prepare request with email not in the activity
        Act: DELETE request with nonexistent email
        Assert: Verify 404 status and error message
        """
        # Arrange
        activity_name = "Gym Class"
        email = "nonexistent@mergington.edu"  # Not in Gym Class
        
        # Act
        response = client.delete(f"/activities/{activity_name}/participants/{email}")
        
        # Assert
        assert response.status_code == 404
        assert "Participant not found" in response.json()["detail"]

    def test_remove_from_nonexistent_activity_returns_error(self, client):
        """
        Test that removing from a nonexistent activity returns 404 error.
        
        Arrange: Prepare request with invalid activity name
        Act: DELETE request with nonexistent activity
        Assert: Verify 404 status and error message
        """
        # Arrange
        activity_name = "Nonexistent Activity"
        email = "student@mergington.edu"
        
        # Act
        response = client.delete(f"/activities/{activity_name}/participants/{email}")
        
        # Assert
        assert response.status_code == 404
        assert "Activity not found" in response.json()["detail"]

    def test_remove_response_message_format(self, client):
        """
        Test that remove success response has the correct message format.
        
        Arrange: Create test client with existing participant
        Act: DELETE request to remove participant
        Assert: Verify response message includes both email and activity name
        """
        # Arrange
        activity_name = "Robotics Club"
        email = "ryan@mergington.edu"  # Existing participant
        
        # Act
        response = client.delete(f"/activities/{activity_name}/participants/{email}")
        data = response.json()
        
        # Assert
        assert response.status_code == 200
        assert email in data["message"]
        assert activity_name in data["message"]
