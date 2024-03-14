from signalling_service.api import Api
from signalling_service.core.config import Config
from signalling_service.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
