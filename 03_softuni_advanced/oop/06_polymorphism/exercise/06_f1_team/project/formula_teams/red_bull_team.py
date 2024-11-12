from abc import ABC
from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam, ABC):
    TEAM_SPONSORS = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
    EXPENSES_PER_RACE = 250000

    def __init__(self, budget):
        super().__init__(budget)
        self.budget = budget

    def get_team_sponsors(self):
        return self.TEAM_SPONSORS

    def get_expenses_per_race(self):
        return self.EXPENSES_PER_RACE
