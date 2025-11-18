from . import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    join_date = db.Column(db.Date)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    subscription_status = db.Column(db.String(20))

    team = db.relationship("Team", back_populates="members")
