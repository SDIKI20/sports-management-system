import csv
from datetime import datetime
import os

# التأكد أن مسار التنفيذ هو نفس مسار الملف
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---------- Classes ----------


class Skill:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Skill: {self.name}"


class Member:
    def __init__(
        self,
        member_id,
        full_name,
        email,
        phone,
        address,
        join_date,
        team_name,
        subscription_status,
        **kwargs,
    ):
        self.id = int(member_id)
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        try:
            self.join_date = datetime.strptime(join_date.strip(), "%Y-%m-%d").date()
        except:
            self.join_date = datetime.today().date()
        self.team_name = team_name
        self.subscription_status = subscription_status
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def display_profile(self):
        print(f"\n--- Member Profile ---")
        print(f"Name: {self.full_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Team: {self.team_name}")
        print(f"Subscription: {self.subscription_status}")
        print(f"Skills: {', '.join([s.name for s in self.skills]) or 'None'}")


class Team:
    def __init__(
        self, team_id=None, team_name=None, coach_name=None, team_type=None, **kwargs
    ):
        self.id = int(team_id) if team_id else None
        self.team_name = team_name
        self.coach_name = coach_name
        self.team_type = team_type
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def show_team(self):
        print(f"\n=== Team: {self.team_name} ===")
        print(f"Coach: {self.coach_name}")
        print(f"Members: {len(self.members)}")
        for m in self.members:
            print(f" - {m.full_name}")


class Subscription:
    def __init__(self, member_id, amount, date, status, **kwargs):
        self.member_id = int(member_id)
        try:
            self.amount = float(amount)
        except:
            self.amount = 0.0
        try:
            self.date = datetime.strptime(date.strip(), "%Y-%m-%d").date()
        except:
            self.date = datetime.today().date()
        self.status = status

    def __str__(self):
        return (
            f"Subscription({self.member_id}, {self.amount}, {self.date}, {self.status})"
        )


class Event:
    def __init__(
        self,
        event_id=None,
        event_name=None,
        event_date=None,
        location=None,
        participants=None,
        organizer=None,
        **kwargs,
    ):
        self.id = int(event_id) if event_id else None
        self.event_name = event_name
        try:
            self.event_date = datetime.strptime(event_date.strip(), "%Y-%m-%d").date()
        except:
            self.event_date = datetime.today().date()
        self.location = location
        self.organizer = organizer if organizer else "Unknown"
        if isinstance(participants, str):
            self.participants = [
                p.strip() for p in participants.split(",") if p.strip()
            ]
        elif isinstance(participants, list):
            self.participants = participants
        else:
            self.participants = []

    def register(self, member):
        self.participants.append(member)

    def show_event(self):
        print(f"\n📅 Event: {self.event_name}")
        print(f"Date: {self.event_date}")
        print(f"Organizer: {self.organizer}")
        print(f"Participants: {len(self.participants)}")


# ---------- Data Loading ----------


def load_csv(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_data():
    # تحميل البيانات من مجلد data/
    members_data = load_csv("data/members_cleaned_extended.csv")
    skills_data = load_csv("data/skills.csv")
    teams_data = load_csv("data/teams.csv")
    subs_data = load_csv("data/subscriptions.csv")
    events_data = load_csv("data/event.csv")

    # تنظيف الأعمدة (إزالة المسافات)
    for sheet in [members_data, skills_data, teams_data, subs_data, events_data]:
        for row in sheet:
            for key in list(row.keys()):
                row[key.strip()] = row.pop(key)

    # إنشاء الفرق أولاً
    teams = {}
    for t in teams_data:
        team_name = t.get("team_name", "").strip()
        if team_name:
            teams[team_name] = Team(
                team_id=t.get("team_id"),
                team_name=team_name,
                coach_name=t.get("coach_name", t.get("coach", "Unknown")),
                team_type=t.get("team_type", "Football"),
            )

    # إنشاء الأعضاء
    members = {}
    for m in members_data:
        member = Member(
            member_id=m["member_id"],
            full_name=m.get("full_name", ""),
            email=m.get("email", ""),
            phone=m.get("phone", ""),
            address=m.get("address", ""),
            join_date=m.get("join_date", "2024-01-01"),
            team_name=m.get("team_name", "General"),  # سيتم تحديثه لاحقاً
            subscription_status=m.get("subscription_status", "inactive"),
        )
        members[int(m["member_id"])] = member

    # **الجزء المهم: ربط الأعضاء بالفرق باستخدام teams.csv**
    member_team_mapping = {}
    for t in teams_data:
        member_id = t.get("member_id")
        team_name = t.get("team_name", "").strip()
        if member_id and team_name:
            member_team_mapping[int(member_id)] = team_name

    # الآن ربط كل عضو بفريقه الصحيح
    for member_id, member in members.items():
        if member_id in member_team_mapping:
            team_name = member_team_mapping[member_id]
            if team_name in teams:
                teams[team_name].add_member(member)
                member.team_name = team_name  # تحديث اسم الفريق للعضو
            else:
                print(f"تحذير: فريق '{team_name}' غير موجود للعضو {member.full_name}")
        else:
            print(f"تحذير: لا يوجد فريق للعضو {member.full_name} (ID: {member_id})")

    # إنشاء المهارات
    skills = [Skill(s.get("skill_name", "Unknown")) for s in skills_data]

    # توزيع المهارات على الأعضاء
    members_list = list(members.values())
    for i, s in enumerate(skills):
        member = members_list[i % len(members_list)]
        member.add_skill(s)

    # إنشاء الاشتراكات
    subscriptions = [Subscription(**s) for s in subs_data]

    # إنشاء الأحداث
    events = [Event(**e) for e in events_data]

    # تسجيل كل الأعضاء في الحدث الأول
    if events:
        for m in members.values():
            events[0].register(m.full_name)

    return members, teams, subscriptions, events


# ---------- Display ----------

if __name__ == "__main__":
    members, teams, subs, events = load_data()

    print("\n--- DATA SUMMARY ---")
    print(
        f"Members: {len(members)} | Teams: {len(teams)} | Events: {len(events)} | Subscriptions: {len(subs)}"
    )

    # عرض كل الفرق
    for t in teams.values():
        t.show_team()

    # عرض أول عضو
    list(members.values())[0].display_profile()

    # عرض أول حدث
    if events:
        events[0].show_event()

    # حساب الدخل
    total_income = sum(s.amount for s in subs if s.status.lower() == "paid")
    print(f"\n💰 Total Income: {total_income:.2f} DA")
