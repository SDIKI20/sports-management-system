from flask import Blueprint, render_template, request, redirect, url_for
from models.subscription import Subscription
from models.member import Member
from models import db

subscription_bp = Blueprint('subscription', __name__)

@subscription_bp.route('/subscriptions')
def list_subscriptions():
    subs = Subscription.query.all()
    members = Member.query.all()
    return render_template('subscriptions.html', subscriptions=subs, members=members)

@subscription_bp.route('/subscriptions/add', methods=['POST'])
def add_subscription():
    member_id = request.form['member_id']
    amount = request.form['amount']
    date = request.form['date']
    status = request.form['status']

    new_sub = Subscription(member_id=member_id, amount=amount, date=date, status=status)
    db.session.add(new_sub)
    db.session.commit()
    return redirect(url_for('subscription.list_subscriptions'))

@subscription_bp.route('/subscriptions/delete/<int:id>')
def delete_subscription(id):
    sub = Subscription.query.get_or_404(id)
    db.session.delete(sub)
    db.session.commit()
    return redirect(url_for('subscription.list_subscriptions'))
