from project.clients.base_client import BaseClient


class VIPClient(BaseClient):

    def __init__(self, name: str) -> None:
        super().__init__(name=name, membership_type="VIP")

    def earning_points(self, order_amount: float):
        points_earned = int(order_amount // 5)
        self.points += points_earned
        return points_earned
