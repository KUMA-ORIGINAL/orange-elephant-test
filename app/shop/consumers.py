import json
from channels.generic.websocket import AsyncWebsocketConsumer


class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("users", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("users", self.channel_name)

    async def user_created(self, event):
        user = event['user']
        await self.send(text_data=json.dumps({
            'message': f"New user created: {user}"
        }))


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("orders", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("orders", self.channel_name)

    async def order_created(self, event):
        order = event['order']
        await self.send(text_data=json.dumps({
            'message': f"New order created: Order #{order}"
        }))
