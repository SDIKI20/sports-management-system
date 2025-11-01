from abc import ABC, abstractmethod

class Registrable(ABC):
    @abstractmethod
    def register_member(self, member):
        pass
