class Team:
    """Classe représentant une équipe sportive"""

    def __init__(self, team_id, team_name, coach_name, team_type):
        self.id = int(team_id)
        self.team_name = team_name
        self.coach_name = coach_name
        self.team_type = team_type
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def show_team(self):
        print(f"\n=== Équipe: {self.team_name} ===")
        print(f"Coach: {self.coach_name}")
        print(f"Type: {self.team_type}")
        print(f"Membres ({len(self.members)}):")
        for m in self.members:
            print(f" - {m.full_name}")
