from flask import Blueprint, render_template, request, redirect, url_for
from models.member import Member
from models.team import Team
from models import db

member_bp = Blueprint('member', __name__)

@member_bp.route('/members')
def list_members():
    members = Member.query.all()
    return render_template('members.html', members=members)

@member_bp.route('/members/add', methods=['POST'])
def add_member():
    full_name = request.form['full_name']
    email = request.form['email']
    phone = request.form['phone']
    team_id = request.form.get('team_id')
    new_member = Member(full_name=full_name, email=email, phone=phone, team_id=team_id)
    db.session.add(new_member)
    db.session.commit()
    return redirect(url_for('member.list_members'))
