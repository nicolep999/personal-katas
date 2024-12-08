from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:

    VALID_WAITERS = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    VALID_CLIENTS = {"VIPClient": VIPClient, "RegularClient": RegularClient}

    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_WAITERS:
            return f"{waiter_type} is not a recognized waiter type."
        if waiter_name in [waiter.name for waiter in self.waiters]:
            return f"{waiter_name} is already on the staff."
        self.waiters.append(self.VALID_WAITERS[waiter_type](waiter_name, hours_worked))
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENTS:
            return f"{client_type} is not a recognized client type."
        if client_name in [client.name for client in self.clients]:
            return f"{client_name} is already a client."
        self.clients.append(self.VALID_CLIENTS[client_type](client_name))
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = next(
            (waiter for waiter in self.waiters if waiter.name == waiter_name), None
        )
        if not waiter:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = next(
            (client for client in self.clients if client.name == client_name), None
        )
        if not client:
            return f"{client_name} is not a registered client."
        return f"{client_name} earned {client.earning_points(order_amount)} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = next(
            (client for client in self.clients if client.name == client_name), None
        )
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        discount, points = client.apply_discount()
        return (
            f"{client_name} received a {discount}% discount. Remaining points {points}"
        )

    def generate_report(self):
        result = "$$ Monthly Report $$\n"
        result += f"Total Earnings: ${sum([waiter.calculate_earnings() for waiter in self.waiters]):.2f}\n"
        result += f"Total Clients Unused Points: {sum([client.points for client in self.clients])}\n"
        result += f"Total Clients Count: {len(self.clients)}\n"
        result += f"** Waiter Details **\n"
        sorted_waiters = sorted(
            self.waiters, key=lambda waiter: waiter.calculate_earnings(), reverse=True
        )
        for waiter in sorted_waiters:
            result += str(waiter)
        return result
