class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}  # Using int for mana_cost
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:  # mana_cost as int
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return (
                f"Skill {skill_name} added to the collection of the player {self.name}"
            )
        return "Skill already added"

    def player_info(self) -> str:
        result = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
            *[f"==={skill} - {self.skills[skill]}" for skill in self.skills],
        ]
        return "\n".join(result)
