from fastapi.testclient import TestClient
import pytest

from signalling_service.core.config import Config
from signalling_service.core.service_container import ServiceContainer  # Import your FastAPI app
from signalling_service.signalling_service import SignallingService


@pytest.mark.asyncio
async def test_websocket_connect():
    config = Config()
    service = SignallingService(config, service_container=ServiceContainer(config))
    client = TestClient(service.api)
    client_id = "meow"
    with client.websocket_connect(f"/connect/{client_id}") as websocket:
        data = websocket.receive_text()
        assert f"WELCOME {client_id}" == data
