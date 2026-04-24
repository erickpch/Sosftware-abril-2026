from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = "notificacion"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "Conectado al grupo"
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print("Desconectado:", close_code)

    async def evento(self, text_data):

        await self.send(text_data=json.dumps({
            "message": text_data
        }))