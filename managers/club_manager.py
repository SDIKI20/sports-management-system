from managers.event_manager import EventManager
from managers.subscription_manager import SubscriptionManager
from models.member import Member
from models.skill import Skill
from models.team import Team

class ClubManager:
    """Classe principale qui gère le club sportif"""

    def __init__(self):
        self.members = []
        self.teams = []
        self.event_manager = EventManager()
        self.subscription_manager = SubscriptionManager()

    # ---------- Gestion des membres ----------
    def add_member(self, member: Member):
        self.members.append(member)

    def assign_skill(self, member_id, skill: Skill):
        for m in self.members:
            if m.id == member_id:
                m.add_skill(skill)
                print(f"Skill '{skill.name}' ajouté à {m.full_name}")
                break

    def display_all_members(self):
        print("\n=== Liste des membres ===")
        for m in self.members:
            print(f"{m.id} - {m.full_name} ({m.team_name}) - {m.subscription_status}")
        print("==========================\n")

    # ---------- Gestion des équipes ----------
    def add_team(self, team: Team):
        self.teams.append(team)

    def assign_member_to_team(self, member_id, team_name):
        for m in self.members:
            if m.id == member_id:
                for t in self.teams:
                    if t.team_name == team_name:
                        t.add_member(m)
                        m.team_name = team_name
                        print(f"{m.full_name} ajouté à l'équipe {team_name}")
                        return
        print("❌ Membre ou équipe introuvable.")

    def show_all_teams(self):
        for team in self.teams:
            team.show_team()

    # ---------- Gestion des événements ----------
    def add_event(self, event):
        self.event_manager.add_event(event)

    def show_all_events(self):
        self.event_manager.show_all()

    # ---------- Gestion des abonnements ----------
    def add_subscription(self, subscription):
        self.subscription_manager.add_subscription(subscription)

    def show_subscriptions(self):
        self.subscription_manager.list_all()
