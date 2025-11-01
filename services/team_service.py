class TeamService:
    def assign_member_to_team(self, member, team):
        team.add_member(member)
        member.team_name = team.team_name
