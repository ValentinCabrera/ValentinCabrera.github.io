from channels.generic.websocket import AsyncWebsocketConsumer
import json

class VideoStreamingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Establecer la conexión WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Manejar la desconexión del WebSocket
        pass

    async def receive(self, text_data):
        # Manejar los fragmentos de video recibidos del cliente
        fragment_data = json.loads(text_data)
        # Procesar y transmitir los fragmentos de video a otros clientes conectados
        await self.send(text_data=json.dumps(fragment_data))
