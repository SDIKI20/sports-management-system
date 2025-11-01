from models.event import Event, Trip, Meeting, Competition

class EventManager:
    """Gère la logique métier des événements"""

    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        """Ajoute un événement à la liste"""
        self.events.append(event)

    def display_event_details(self, event: Event):
        """Affiche les détails d’un événement (principe de substitution de Liskov)"""
        print("\n" + "=" * 50)
        print(f"Event ID: {event.id}")
        print(f"Date: {event.event_date}")
        print(f"Location: {event.location}")
        print(f"Description: {event.describe()}")
        print(f"Participants: {len(event.participants)}")
        print("=" * 50 + "\n")

    def show_all(self):
        """Affiche tous les événements"""
        for event in self.events:
            self.display_event_details(event)


# --- Test local ---
if __name__ == "__main__":
    trip = Trip(1, "Summer Camp", "2025-07-15", "Bouira", "Tikjda", "Bus")
    meeting = Meeting(2, "Annual Assembly", "2025-06-01", "Club House", "Budget Review", 2)
    competition = Competition(3, "Football Tournament", "2025-08-20", "Stadium", "Football", "5000 DA")

    manager = EventManager()
    for e in [trip, meeting, competition]:
        manager.add_event(e)

    manager.show_all()
