from pogo_api.endpoint import PostEndpoint

from signalling_service.domain.websocket_service import WebSocketService


class AcceptCall(PostEndpoint):
    def __init__(self, websocket_service: WebSocketService) -> None:
        self.websocket_service = websocket_service

    @property
    def path(self) -> str:
        return "/calls/accept"

    async def endpoint(self, client_id: str) -> str:
        # await self.websocket_service.send_message("BLA, accpeted your call!", client_id)
        return f"{client_id}: someone accpeted your call!"
