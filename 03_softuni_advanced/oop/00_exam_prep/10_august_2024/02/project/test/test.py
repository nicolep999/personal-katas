from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class SoccerPlayerTestCase(TestCase):
    def test_init(self):
        player = SoccerPlayer("Garnacho", 20, 5, "Manchester United")
        self.assertEqual(player.name, "Garnacho")
        self.assertEqual(player.age, 20)
        self.assertEqual(player.goals, 5)
        self.assertEqual(player.team, "Manchester United")
        self.assertEqual(player.achievements, {})

    def test_name(self):
        with self.assertRaises(ValueError) as ex:
            player = SoccerPlayer("Tests", 20, 5, "Manchester United")
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_age(self):
        with self.assertRaises(ValueError) as ex:
            player = SoccerPlayer("Garnacho", 15, 5, "Manchester United")
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_valid_team(self):
        with self.assertRaises(ValueError) as ex:
            player = SoccerPlayer("Garnacho", 20, 5, "Manchester City")
        self.assertEqual(
            str(ex.exception),
            "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!",
        )

    def test_change_team(self):
        player = SoccerPlayer("Garnacho", 20, 5, "Manchester United")
        self.assertEqual(player.change_team("Barcelona"), "Team successfully changed!")

    def test_add_new_achievement(self):
        player = SoccerPlayer("Garnacho", 20, 5, "Manchester United")
        self.assertEqual(
            player.add_new_achievement("Golden Boot"),
            "Golden Boot has been successfully added to the achievements collection!",
        )

    def test__lt__(self):
        player1 = SoccerPlayer("Garnacho", 20, 5, "Manchester United")
        player2 = SoccerPlayer("Rooney", 20, 3, "Manchester United")
        result = player1.__lt__(player2)
        self.assertEqual(result, "Garnacho is a better goal scorer than Rooney.")
        player2.goals = 7
        result = player1.__lt__(player2)
        self.assertEqual(
            result, "Rooney is a top goal scorer! S/he scored more than Garnacho."
        )


if __name__ == "__main__":
    main()
