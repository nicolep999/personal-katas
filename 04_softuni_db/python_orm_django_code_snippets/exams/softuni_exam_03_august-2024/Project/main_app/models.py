from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

# Create your models here.
from main_app.mixins import LaunchDateMixin
from main_app.managers import AstronautManager


class BaseObject(models.Model):

    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Astronaut(BaseObject):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(r"^\d+$"),
        ],
    )
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(blank=True, null=True)
    spacewalks = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    objects = AstronautManager()


class Spacecraft(BaseObject, LaunchDateMixin):
    manufacturer = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(validators=[MinValueValidator(0.0)])


class Mission(BaseObject, LaunchDateMixin):

    class StatusChoices(models.TextChoices):
        PLANNED = "Planned"
        ONGOING = "Ongoing"
        COMPLETED = "Completed"

    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=9, default=StatusChoices.PLANNED, choices=StatusChoices.choices
    )
    spacecraft = models.ForeignKey(Spacecraft, on_delete=models.CASCADE)
    astronauts = models.ManyToManyField(Astronaut)
    commander = models.ForeignKey(
        Astronaut,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="commander",
    )
