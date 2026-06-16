"""
Tests for the root endpoint (GET /).

Tests the redirect behavior of the root endpoint.
"""

import pytest


class TestRoot:
    """Tests for the root endpoint (GET /)."""

    def test_root_redirects_to_index_html(self, client):
        """
        Test that GET / redirects to /static/index.html.
        
        Arrange: Create test client
        Act: GET /
        Assert: Verify 307 redirect response to /static/index.html
        """
        # Arrange
        # client fixture is injected via pytest
        
        # Act
        response = client.get("/", follow_redirects=False)
        
        # Assert
        assert response.status_code == 307
        assert response.headers["location"] == "/static/index.html"
