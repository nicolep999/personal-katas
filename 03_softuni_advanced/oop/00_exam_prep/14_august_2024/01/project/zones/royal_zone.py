from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    type = "Royal"

    def __init__(self, code: str):
        super().__init__(code, volume=10)

    def zone_info(self):
        result = "@Royal Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += f"Battleships currently in the Royal Zone: {len(self.ships)}, {len([ship for ship in self.ships if isinstance(ship, PirateBattleship)])} out of them are Pirate Battleships.\n"
        sorted_ships = self.get_ships()
        if sorted_ships:
            result += f"#{', '.join([ship.name for ship in sorted_ships])}#\n"
        return result
