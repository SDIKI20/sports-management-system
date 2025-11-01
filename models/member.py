class Member:
    """Représente un membre du club sportif."""

    def __init__(self, member_id, full_name, email, phone, address, join_date, team_name, subscription_status):
        self.id = int(member_id)
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.team_name = team_name
        self.subscription_status = subscription_status
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def __str__(self):
        return f"{self.full_name} ({self.team_name})"
