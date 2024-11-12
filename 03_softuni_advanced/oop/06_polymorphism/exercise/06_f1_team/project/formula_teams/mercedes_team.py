from abc import ABC
from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam, ABC):
    TEAM_SPONSORS = {
        "Petronas": {1: 1000000, 3: 500000},
        "TeamViewer": {5: 100000, 7: 50000},
    }
    EXPENSES_PER_RACE = 200000

    def __init__(self, budget):
        super().__init__(budget)
        self.budget = budget

    def get_team_sponsors(self):
        return self.TEAM_SPONSORS

    def get_expenses_per_race(self):
        return self.EXPENSES_PER_RACE
