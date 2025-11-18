from flask import Blueprint, render_template, request, redirect, url_for
from models.team import Team
from models import db

team_bp = Blueprint('team', __name__)

@team_bp.route('/teams')
def list_teams():
    teams = Team.query.all()
    return render_template('teams.html', teams=teams)

@team_bp.route('/teams/add', methods=['POST'])
def add_team():
    name = request.form['name']
    coach_name = request.form['coach_name']
    type = request.form['type']
    new_team = Team(name=name, coach_name=coach_name, type=type)
    db.session.add(new_team)
    db.session.commit()
    return redirect(url_for('team.list_teams'))

@team_bp.route('/teams/delete/<int:id>')
def delete_team(id):
    team = Team.query.get_or_404(id)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('team.list_teams'))
