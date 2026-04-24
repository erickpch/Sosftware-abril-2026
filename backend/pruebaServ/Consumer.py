from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "Conectado correctamente"
        }))

    async def disconnect(self, close_code):
        # Podés manejar limpieza acá si usás grupos
        print("Desconectado:", close_code)

    async def receive(self, text_data):
        data = json.loads(text_data)
        mensaje = data.get("message", "")

        # Reenvía el mensaje (echo simple)
        await self.send(text_data=json.dumps({
            "message": f"Recibido: {mensaje}"
        }))