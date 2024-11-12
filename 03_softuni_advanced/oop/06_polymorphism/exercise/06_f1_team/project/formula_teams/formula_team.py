from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self._budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self._budget = value

    @abstractmethod
    def get_team_sponsors(self):
        pass

    @abstractmethod
    def get_expenses_per_race(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0
        sponsors = self.get_team_sponsors()
        for payouts in sponsors.values():
            qualifying_payouts = [
                payout for position, payout in payouts.items() if race_pos <= position
            ]
            if qualifying_payouts:
                revenue += max(qualifying_payouts)

        expenses = self.get_expenses_per_race()
        self.budget += revenue - expenses
        return f"The revenue after the race is {revenue-expenses}$. Current budget {self.budget}$"
