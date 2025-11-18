from flask import Flask
from config import Config
from models import db
from controllers.member_controller import member_bp
from controllers.team_controller import team_bp
from controllers.event_controller import event_bp
from controllers.subscription_controller import subscription_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Enregistrement des Blueprints
app.register_blueprint(member_bp)
app.register_blueprint(team_bp)
app.register_blueprint(event_bp)
app.register_blueprint(subscription_bp)

@app.route('/')
def home():
    return """
    <h1>🏆 Système de Gestion d'Association</h1>
    <ul>
        <li><a href='/members'>👥 Membres</a></li>
        <li><a href='/teams'>⚽ Équipes</a></li>
        <li><a href='/subscriptions'>💰 Abonnements</a></li>
        <li><a href='/events'>📅 Événements</a></li>
    </ul>
    """

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
