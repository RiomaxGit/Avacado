import json
import pytest
from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator
from django.contrib.auth import get_user_model
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chatlogic.consumer import ChatConsumer
from django.test import TestCase
from django.contrib.auth.models import User

# A helper function to create a user
@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="password123")

# Test setup for WebSocket communication
@pytest.fixture
def communicator():
    # Returns an instance of WebsocketCommunicator for a WebSocket test connection
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "ws/chat/")
    return communicator

# Test that the WebSocket connects successfully
@pytest.mark.asyncio
async def test_websocket_connect(communicator, user):
    # Simulate a WebSocket connection
    connected, subprotocol = await communicator.connect()

    # Assert that the connection is established
    assert connected
    assert subprotocol is None  # No subprotocols for now

    # Send a message after connecting
    message = {
        "message": "Hello, World!",
        "username": user.username,
        "time": "2024-12-10 12:00:00"
    }
    await communicator.send_json_to(message)

    # Receive message
    response = await communicator.receive_json_from()

    # Assert the message received is the one that was sent
    assert response["message"] == "Hello, World!"
    assert response["username"] == user.username
    assert response["time"] == "2024-12-10 12:00:00"

    # Disconnect after test
    await communicator.disconnect()

# Test WebSocket disconnects
@pytest.mark.asyncio
async def test_websocket_disconnect(communicator, user):
    # Connect to WebSocket
    connected, subprotocol = await communicator.connect()
    assert connected

    # Disconnect and verify it works without errors
    await communicator.disconnect()
    # No assertion needed for disconnect, but you can check the layer/discard actions in consumers if you need.

# Test for views requiring login
class ChatViewsTest(TestCase):
    def test_redirect_if_not_logged_in(self):
        # Check that a user who is not logged in gets redirected to the login page
        response = self.client.get("/")
        self.assertRedirects(response, "/auth/login/")

    def test_access_chat_if_logged_in(self):
        # Create and log in a user
        user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        # Test that logged-in users can access the chat page
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "avacadoPage.html")

    def test_logout_redirect(self):
        # Ensure that the logout view correctly redirects to the login page
        response = self.client.get("/auth/logout/")
        self.assertRedirects(response, "/auth/login/")
