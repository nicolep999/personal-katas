from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ivan", 10, 10, 10)
        self.enemy = Hero("Pesho", 10, 10, 10)

    def test_init(self):
        self.assertEqual(self.hero.username, "Ivan")
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 10)
        self.assertEqual(self.hero.damage, 10)

    def test_str(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\nHealth: {self.hero.health}\nDamage: {self.hero.damage}\n"
        self.assertEqual(str(self.hero), expected)

    def test_battle_same_username(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_your_health_is_lower_than_or_equal_to_0(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(
            "Your health is lower than or equal to 0. You need to rest",
            str(ex.exception),
        )

    def test_battle_enemy_health_is_lower_than_or_equal_to_0(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(
            f"You cannot fight {self.enemy.username}. He needs to rest",
            str(ex.exception),
        )

    def test_battle_win_condition(self):
        self.enemy.level = 2
        self.enemy.health = 1
        self.enemy.damage = 0
        result = self.hero.battle(self.enemy)
        self.assertEqual("You win", result)
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 15)
        self.assertEqual(self.hero.damage, 15)

    def test_battle_lose_condition(self):
        self.enemy.level = 22
        self.enemy.health = 111
        self.enemy.damage = 110
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)

    def test_battle_draw(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.hero.health, -90)
        self.assertEqual(self.enemy.health, -90)

    def test_battle_your_level_increases_after_win(self):
        self.enemy.level = 2
        self.enemy.health = 1
        self.enemy.damage = 0
        self.hero.battle(self.enemy)
        self.assertEqual(self.hero.level, 11)

    def test_battle_your_health_increases_after_win(self):
        self.enemy.level = 2
        self.enemy.health = 1
        self.enemy.damage = 0
        self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health, 15)

    def test_battle_your_damage_increases_after_win(self):
        self.enemy.level = 2
        self.enemy.health = 1
        self.enemy.damage = 0
        self.hero.battle(self.enemy)
        self.assertEqual(self.hero.damage, 15)


if __name__ == "__main__":
    main()
