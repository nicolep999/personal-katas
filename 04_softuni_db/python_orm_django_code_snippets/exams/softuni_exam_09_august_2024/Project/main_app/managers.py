from main_app.models import models


class HouseManager(models.Manager):

    def get_houses_by_dragons_count(self):
        return self.annotate(dragon_count=models.Count("dragon")).order_by(
            "-dragon_count", "name"
        )
