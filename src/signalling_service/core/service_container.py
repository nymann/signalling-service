from signalling_service.core.config import Config
from signalling_service.domain.websocket_service import WebSocketService


class ServiceContainer:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.websocket_service = WebSocketService()
