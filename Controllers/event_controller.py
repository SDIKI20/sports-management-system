from flask import Blueprint, render_template, request, redirect, url_for
from models.event import Event
from models import db

event_bp = Blueprint('event', __name__)

@event_bp.route('/events')
def list_events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@event_bp.route('/events/add', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    organizer = request.form['organizer']
    new_event = Event(name=name, date=date, location=location, organizer=organizer)
    db.session.add(new_event)
    db.session.commit()
    return redirect(url_for('event.list_events'))

@event_bp.route('/events/delete/<int:id>')
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('event.list_events'))
