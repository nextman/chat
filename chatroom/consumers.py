from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils.html import escape


class ChatConsumer(WebsocketConsumer):
    groups = ["public", ]

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)("public", self.channel_name)
        async_to_sync(self.channel_layer.group_send)("public", self.pack_message("user join channel."))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_send)("public", self.pack_message("user leave channel."))
        async_to_sync(self.channel_layer.group_discard)("public", self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)("public", self.pack_message(text_data))

    def pack_message(self, text):
        return {"type": "send.message",
                "text": escape(text)}

    def send_message(self, event):
        self.send(text_data=event["text"])
