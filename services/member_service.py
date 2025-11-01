class MemberService:
    def display_profile(self, member):
        print(f"\n--- Member Profile ---")
        print(f"Name: {member.full_name}")
        print(f"Email: {member.email}")
        print(f"Phone: {member.phone}")
        print(f"Team: {member.team_name}")
        skills = ', '.join([s.name for s in member.skills])
        print(f"Skills: {skills or 'None'}")
