import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission
from django.utils import timezone


# Create queries within functions
def get_astronauts(search_string=None) -> str:

    if search_string is None:
        return ""

    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by("name")

    if not astronauts.exists():
        return ""

    result = [
        f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {'Active' if astronaut.is_active else 'Inactive'}"
        for astronaut in astronauts
    ]

    return "\n".join(result)


def get_top_astronaut() -> str:

    if not Mission.objects.exists():
        return "No data."

    astronaut = (
        Astronaut.objects.get_astronauts_by_missions_count()
        .order_by("-mission_count", "phone_number")
        .first()
    )
    if not astronaut or astronaut.mission_count == 0:
        return "No data."

    return f"Top Astronaut: {astronaut.name} with {astronaut.mission_set.count()} missions."


def get_top_commander() -> str:

    if not Mission.objects.filter(commander__isnull=False).exists():
        return "No data."

    commander = (
        Astronaut.objects.annotate(commanded_count=Count("commander"))
        .filter(commanded_count__gt=0)
        .order_by("-commanded_count", "phone_number")
        .first()
    )

    if not commander:
        return "No data."

    return f"Top Commander: {commander.name} with {commander.commanded_count} commanded missions."


def get_last_completed_mission():
    last_completed_mission = (
        Mission.objects.filter(status="Completed").order_by("-launch_date").first()
    )

    if not last_completed_mission:
        return "No data."

    commander_name = (
        last_completed_mission.commander.name
        if last_completed_mission.commander
        else "TBA"
    )

    astronauts = [
        astronaut.name
        for astronaut in last_completed_mission.astronauts.all().order_by("name")
    ]

    total_spacewalks = sum(
        astronaut.spacewalks for astronaut in last_completed_mission.astronauts.all()
    )

    return f"The last completed mission is: {last_completed_mission.name}. Commander: {commander_name}. Astronauts: {', '.join(astronauts)}. Spacecraft: {last_completed_mission.spacecraft.name}. Total spacewalks: {total_spacewalks}."


def get_most_used_spacecraft():
    spacecraft = (
        Spacecraft.objects.annotate(
            num_missions=Count("mission", distinct=True),
            num_astronauts=Count("mission__astronauts", distinct=True),
        )
        .order_by("-num_missions", "name")
        .first()
    )

    if not spacecraft or spacecraft.num_missions == 0:
        return "No data."
    return f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, used in {spacecraft.num_missions} missions, astronauts on missions: {spacecraft.num_astronauts}."


def decrease_spacecrafts_weight():
    spacecrafts_to_update = Spacecraft.objects.filter(
        mission__status="Planned", weight__gte=200.0
    ).distinct()

    if not spacecrafts_to_update.exists():
        return "No changes in weight."

    for spacecraft in spacecrafts_to_update:
        spacecraft.weight -= 200.0
        spacecraft.save()

    avg_weight = Spacecraft.objects.aggregate(avg=Avg("weight"))["avg"]

    return (
        f"The weight of {spacecrafts_to_update.count()} spacecrafts has been decreased. "
        f"The new average weight of all spacecrafts is {avg_weight:.1f}kg"
    )
