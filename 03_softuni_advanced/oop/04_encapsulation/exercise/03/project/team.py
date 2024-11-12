from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player._name} joined team {self.__name}"
        return f"Player {player._name} has already joined"

    def remove_player(self, player_name: str):
        player = next((p for p in self.__players if p._name == player_name), None)
        if player:
            self.__players.remove(player)
            return player
        return f"Player {player_name} not found"
