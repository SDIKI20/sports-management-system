class CsvStorage:
    """Gère la persistance des membres"""
    def __init__(self, storage):
        self.storage = storage

    def save(self, member):
        self.storage.save(member)

    def load_all(self, filename):
        return self.storage.load(filename)