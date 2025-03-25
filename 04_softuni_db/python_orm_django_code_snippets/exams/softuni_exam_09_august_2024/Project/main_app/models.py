from datetime import date

from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
from django.db import models
from django.utils.timezone import now
from main_app.managers import HouseManager

# Create your models here.


class WinsMixin(models.Model):
    wins = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    name = models.CharField(
        max_length=80, validators=[MinLengthValidator(5)], unique=True
    )
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class House(BaseModel, WinsMixin):
    motto = models.TextField(null=True, blank=True)
    is_ruling = models.BooleanField(default=False)
    castle = models.CharField(max_length=80, null=True, blank=True)

    objects = HouseManager()


class Dragon(BaseModel, WinsMixin):

    class BreathChoices(models.TextChoices):
        FIRE = "Fire"
        ICE = "Ice"
        LIGHTING = "Lightning"
        UNKNOWN = "Unknown"

    power = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
        default=1.0,
    )
    breath = models.CharField(
        choices=BreathChoices.choices, default=BreathChoices.UNKNOWN, max_length=9
    )
    is_healthy = models.BooleanField(default=True)
    birth_date = models.DateField(default=date.today)
    house = models.ForeignKey("House", on_delete=models.CASCADE)


class Quest(BaseModel):
    code = models.CharField(
        max_length=4,
        unique=True,
        validators=[RegexValidator(regex=r"^[A-Za-z#]{4}$")],
    )
    reward = models.FloatField(default=100.0)
    start_time = models.DateTimeField(default=now)
    dragons = models.ManyToManyField("Dragon")
    host = models.ForeignKey("House", on_delete=models.CASCADE)
