from . import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    coach_name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    members = db.relationship("Member", back_populates="team", lazy=True)
