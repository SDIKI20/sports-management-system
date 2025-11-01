from abc import ABC, abstractmethod

class Storage(ABC):
    """Interface pour la persistance des données"""

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self, filename):
        pass
