import logging

from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from pogo_api.websocket_endpoint import WebSocketEndpoint

from signalling_service.domain.websocket_service import WebSocketService


class Connect(WebSocketEndpoint):
    def __init__(self, websocket_service: WebSocketService) -> None:
        self.websocket_service = websocket_service

    @property
    def path(self) -> str:
        return "/connect/{client_id}"

    async def endpoint(self, websocket: WebSocket, client_id: str) -> None:
        await self.websocket_service.connect(websocket, client_id)
        await self.websocket_service.send_message("WELCOME " + client_id, client_id)
        try:
            while True:
                await websocket.receive_text()
        except WebSocketDisconnect:
            logging.info(f"{client_id} disconnected")
        except Exception as e:
            logging.warn("Received unexpected exception from websocket", exc_info=e)
        finally:
            self.websocket_service.disconnect(client_id)
