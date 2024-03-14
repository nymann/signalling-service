from signalling_service.core.config import Config
from signalling_service.core.service_container import ServiceContainer
from signalling_service.signalling_service import SignallingService

config = Config()
service_container = ServiceContainer(config=config)
api = SignallingService(config=config, service_container=service_container).api
