from abc import ABC, abstractmethod
from .engine import Engine
from serviceable import Serviceable

class Car(Serviceable, ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine = Engine

    @abstractmethod
    def needs_service(self):
        return super().needs_service
