from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:

    zone_classes = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    ship_classes = {
        "RoyalBattleship": RoyalBattleship,
        "PirateBattleship": PirateBattleship,
    }

    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.zone_classes:
            raise ValueError(f"Invalid zone type!")
        if zone_code in (zone.code for zone in self.zones):
            raise Exception("Zone already exists!")
        self.zones.append(self.zone_classes[zone_type](zone_code))
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.ship_classes:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        self.ships.append(self.ship_classes[ship_type](name, health, hit_strength))
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if len(zone.ships) >= zone.volume:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"
        if ship.type == zone.type:
            ship.is_attacking = True

        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((ship for ship in self.ships if ship.name == ship_name), None)
        if not ship:
            return "No ship with this name!"
        if not ship.is_available:
            return f"The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attacker = max(
            (ship for ship in zone.ships if ship.is_attacking),
            key=lambda s: s.hit_strength,
            default=None,
        )
        target = max(
            (ship for ship in zone.ships if not ship.is_attacking),
            key=lambda s: s.health,
            default=None,
        )

        if not attacker or not target:
            return "Not enough participants. The battle is canceled."

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."
        elif attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."
        else:
            return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{', '.join([ship.name for ship in available_ships])}#\n"
        result += "***Zones Statistics:***\n"
        sorted_zones = sorted(self.zones, key=lambda zone: zone.code)
        result += f"Total Zones: {len(self.zones)}\n"
        for zone in sorted_zones:
            result += zone.zone_info()
        return result
