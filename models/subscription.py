from . import db

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    amount = db.Column(db.Float)
    date = db.Column(db.Date)
    status = db.Column(db.String(20))

    member = db.relationship("Member")
