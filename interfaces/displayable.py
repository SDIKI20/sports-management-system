from abc import ABC, abstractmethod

class Displayable(ABC):
    """Interface pour les objets affichables"""

    @abstractmethod
    def display(self):
        pass
