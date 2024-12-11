# chatlogic/tests.py
import json
from channels.testing import WebsocketCommunicator
from django.test import TestCase
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from chatlogic.consumer import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path


class ChatConsumerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creating a user to simulate an authenticated user
        cls.user = get_user_model().objects.create_user(username='testuser', password='password')

    def setUp(self):
        self.application = ProtocolTypeRouter({
            "websocket": AuthMiddlewareStack(URLRouter([
                path("", ChatConsumer.as_asgi()),
            ])),
        })

    async def test_connect(self):
        # Simulating a WebSocket connection
        communicator = WebsocketCommunicator(self.application, f"ws/chat/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        await communicator.disconnect()

    async def test_receive_and_send_message(self):
        # Simulating a WebSocket connection
        communicator = WebsocketCommunicator(self.application, f"ws/chat/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)

        # Send a message
        message = {
            'message': 'Hello!',
            'username': self.user.username,
            'time': '2024-12-10T10:00:00'
        }
        await communicator.send_json_to(message)

        # Receive the response
        response = await communicator.receive_json_from()
        self.assertEqual(response['message'], 'Hello!')
        self.assertEqual(response['username'], self.user.username)

        await communicator.disconnect()