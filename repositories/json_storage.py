class JsonStorage:
    """Stockage en mémoire pour le test"""
    def __init__(self):
        self.data = []

    def save(self, item):
        self.data.append(item)

    def load(self, filename=None):
        return self.data
