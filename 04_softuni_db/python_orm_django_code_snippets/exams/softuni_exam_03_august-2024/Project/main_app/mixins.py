from main_app.models import models


class LaunchDateMixin(models.Model):
    launch_date = models.DateField()

    class Meta:
        abstract = True
