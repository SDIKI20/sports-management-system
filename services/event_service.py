def display_event_details(event):
    print(f"\n{'='*50}")
    print(f"Event ID: {event.id}")
    print(f"Date: {event.event_date}")
    print(f"Location: {event.location}")
    print(f"Description: {event.describe()}")
    print(f"Participants: {len(event.participants)}")
    print(f"{'='*50}\n")
