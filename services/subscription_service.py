class SubscriptionService:
    def calculate_total(self, subscriptions):
        return sum(s.calculate_amount() for s in subscriptions)
