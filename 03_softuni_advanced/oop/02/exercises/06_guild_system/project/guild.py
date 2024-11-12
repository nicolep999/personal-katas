from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:
            return f"Player {player._name} is already in the guild."
        elif player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player._name} to the guild {self.name}"
        return f"Player {player._name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        player = next((p for p in self.players if p._name == player_name), None)
        if player and player.guild == self.name:
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = [
            f"Guild: {self.name}",
            *[p.player_info() for p in self.players],
        ]
        return "\n".join(result)
