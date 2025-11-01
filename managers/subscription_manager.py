from models.subscription import Subscription, Donation, MonthlySubscription, AnnualSubscription

class SubscriptionManager:
    """Gère les abonnements et les paiements"""

    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, subscription: Subscription):
        """Ajoute un abonnement à la liste"""
        self.subscriptions.append(subscription)

    def calculate_total_income(self):
        """Calcule le revenu total (tous abonnements confondus)"""
        return sum(sub.calculate_amount() for sub in self.subscriptions)

    def list_all(self):
        """Affiche tous les abonnements"""
        print("\n=== Subscriptions Summary ===")
        for sub in self.subscriptions:
            print(f"Member ID: {sub.member_id} | Amount: {sub.amount} | Date: {sub.date} | Status: {sub.status}")
        print(f"💰 Total Income: {self.calculate_total_income():.2f} DA\n")


# --- Test local ---
if __name__ == "__main__":
    subs = [
        Subscription(1, 1000, "2025-05-10", "paid"),
        Donation(2, 5000, "2025-05-11", "paid", "Ali"),
        MonthlySubscription(3, 800, "2025-05-12", "paid", "May"),
        AnnualSubscription(4, 700, "2025-05-13", "paid", "2025")
    ]

    manager = SubscriptionManager()
    for s in subs:
        manager.add_subscription(s)

    manager.list_all()
