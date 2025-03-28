from main_app.models import models


class TennisPlayerManager(models.Manager):

    def get_tennis_players_by_wins_count(self):
        return self.annotate(total_wins=models.Count("winner_player")).order_by(
            "-total_wins", "full_name"
        )
