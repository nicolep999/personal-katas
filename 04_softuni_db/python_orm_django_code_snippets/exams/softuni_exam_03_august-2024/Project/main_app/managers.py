from django.db.models import Count
from main_app.models import models


class AstronautManager(models.Manager):

    def get_astronauts_by_missions_count(self):
        return self.annotate(mission_count=Count("mission")).order_by(
            "-mission_count", "phone_number"
        )
