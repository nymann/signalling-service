import logging

from fastapi import FastAPI
from pogo_api.endpoint import Endpoint

from signalling_service.core.config import Config
from signalling_service.core.service_container import ServiceContainer
from signalling_service.endpoints.calls.accept import AcceptCall
from signalling_service.endpoints.connect import Connect


class SignallingService:
    def __init__(self, config: Config, service_container: ServiceContainer) -> None:
        logging.basicConfig(level=config.log_level, format="%(levelname)s:\t%(asctime)s\t%(message)s")  # noqa: WPS323
        self.api = FastAPI(version=config.version, title=config.title, docs_url="/")
        self._services = service_container
        self._add_endpoints_to_api()
        self._add_websocket_endpoints_to_api()

    def _add_endpoints_to_api(self) -> None:
        endpoints: list[Endpoint] = [AcceptCall(self._services.websocket_service)]
        for endpoint in endpoints:
            endpoint.route.add_to_router(self.api)

    def _add_websocket_endpoints_to_api(self) -> None:
        endpoints = [Connect(websocket_service=self._services.websocket_service)]
        for endpoint in endpoints:
            endpoint.route.add_to_router(self.api)
