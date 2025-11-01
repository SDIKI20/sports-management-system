class Event:
    """Classe de base pour tous les événements"""

    def __init__(self, event_id, event_name, event_date, location):
        self.id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.participants = []

    def describe(self):
        return f"Event: {self.event_name} at {self.location}"

    def register(self, member):
        self.participants.append(member)


class Trip(Event):
    def __init__(self, event_id, event_name, event_date, location, destination, transport_mode):
        super().__init__(event_id, event_name, event_date, location)
        self.destination = destination
        self.transport_mode = transport_mode

    def describe(self):
        return f"Trip to {self.destination} by {self.transport_mode}"


class Meeting(Event):
    def __init__(self, event_id, event_name, event_date, location, agenda, duration):
        super().__init__(event_id, event_name, event_date, location)
        self.agenda = agenda
        self.duration = duration

    def describe(self):
        return f"Meeting: {self.agenda} ({self.duration}h)"


class Competition(Event):
    def __init__(self, event_id, event_name, event_date, location, sport_type, prize):
        super().__init__(event_id, event_name, event_date, location)
        self.sport_type = sport_type
        self.prize = prize

    def describe(self):
        return f"Competition: {self.sport_type} - Prize: {self.prize}"
