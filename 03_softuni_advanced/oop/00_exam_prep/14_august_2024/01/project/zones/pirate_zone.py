from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    type = "Pirate"

    def __init__(self, code: str):
        super().__init__(code, volume=8)

    def zone_info(self):
        result = "@Pirate Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += f"Battleships currently in the Pirate Zone: {len(self.ships)}, {len([ship for ship in self.ships if isinstance(ship, RoyalBattleship)])} out of them are Royal Battleships.\n"
        sorted_ships = self.get_ships()
        if sorted_ships:
            result += f"#{', '.join([ship.name for ship in sorted_ships])}#\n"

        return result
