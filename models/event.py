from . import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.Date)
    location = db.Column(db.String(200))
    organizer = db.Column(db.String(100))
