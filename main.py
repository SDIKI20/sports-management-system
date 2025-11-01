from managers.club_manager import ClubManager
from models.member import Member
from models.team import Team
from models.skill import Skill
from models.event import Trip, Meeting, Competition
from models.subscription import Subscription, Donation, MonthlySubscription, AnnualSubscription

if __name__ == "__main__":
    print("\n=== ⚽ Système de Gestion du Club Sportif ===")

    # Initialisation du club
    club = ClubManager()

    # === Membres ===
    m1 = Member(1, "John Doe", "john@example.com", "12345678", "Rue 1", "2024-01-01", "Aucune", "active")
    m2 = Member(2, "Jane Smith", "jane@example.com", "87654321", "Rue 2", "2024-02-10", "Aucune", "inactive")
    club.add_member(m1)
    club.add_member(m2)

    # Ajout de compétences
    club.assign_skill(1, Skill("Defending"))
    club.assign_skill(2, Skill("Attacking"))

    # === Équipes ===
    t1 = Team(1, "Lions", "Coach Adam", "Football")
    t2 = Team(2, "Eagles", "Coach Ryan", "Basketball")
    club.add_team(t1)
    club.add_team(t2)

    club.assign_member_to_team(1, "Lions")
    club.assign_member_to_team(2, "Eagles")

    # === Événements ===
    trip = Trip(1, "Summer Camp", "2025-07-15", "Bouira", "Tikjda", "Bus")
    meeting = Meeting(2, "Annual Assembly", "2025-06-01", "Club House", "Budget Review", 2)
    competition = Competition(3, "Football Tournament", "2025-08-20", "Stadium", "Football", "5000 DA")

    club.add_event(trip)
    club.add_event(meeting)
    club.add_event(competition)

    # === Abonnements ===
    club.add_subscription(Subscription(1, 1000, "2025-05-10", "paid"))
    club.add_subscription(Donation(2, 5000, "2025-05-11", "paid", "Jane"))
    club.add_subscription(MonthlySubscription(3, 800, "2025-05-12", "paid", "May"))
    club.add_subscription(AnnualSubscription(4, 700, "2025-05-13", "paid", "2025"))

    # === Affichages ===
    club.display_all_members()
    club.show_all_teams()
    club.show_all_events()
    club.show_subscriptions()

    print("\n✅ Programme terminé avec succès.")
