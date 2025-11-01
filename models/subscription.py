class Subscription:
    def __init__(self, member_id, amount, date, status):
        self.member_id = member_id
        self.amount = amount
        self.date = date
        self.status = status

    def calculate_amount(self):
        return self.amount


class Donation(Subscription):
    def __init__(self, member_id, amount, date, status, donor_name):
        super().__init__(member_id, amount, date, status)
        self.donor_name = donor_name

    def calculate_amount(self):
        return self.amount * 0.95  # Réduction fiscale


class MonthlySubscription(Subscription):
    def __init__(self, member_id, amount, date, status, month):
        super().__init__(member_id, amount, date, status)
        self.month = month


class AnnualSubscription(Subscription):
    def __init__(self, member_id, amount, date, status, year):
        super().__init__(member_id, amount, date, status)
        self.year = year

    def calculate_amount(self):
        return self.amount * 12 * 0.9
