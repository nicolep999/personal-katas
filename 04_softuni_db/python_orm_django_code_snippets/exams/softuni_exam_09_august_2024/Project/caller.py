import os
from datetime import datetime, date

import django
from django.db.models import Count, Q, Min, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import House, Dragon, Quest

# Create queries within functions


def get_houses(search_string=None) -> str:
    if search_string is None or not search_string:
        return "No houses match your search."
    houses = House.objects.filter(
        Q(name__istartswith=search_string) | Q(motto__istartswith=search_string)
    ).order_by("-wins", "name")
    if not houses:
        return "No houses match your search."
    result = [
        f"House: {house.name}, wins: {house.wins}, motto: {house.motto if house.motto else 'N/A'}"
        for house in houses
    ]
    return "\n".join(result)


def get_most_dangerous_house() -> str:
    house = (
        House.objects.get_houses_by_dragons_count()
        .order_by("-dragon_count", "name")
        .first()
    )
    if not house or house.dragon_count == 0:
        return "No relevant data."
    ruling_status = "ruling" if house.is_ruling else "not ruling"
    return f"The most dangerous house is the House of {house.name} with {house.dragon_count} dragons. Currently {ruling_status} the kingdom."


def get_most_powerful_dragon() -> str:
    dragon = Dragon.objects.filter(is_healthy=True).order_by("-power", "name").first()
    if not dragon:
        return "No relevant data."
    dragon_quests = dragon.quest_set.count()
    return f"The most powerful healthy dragon is {dragon.name} with a power level of {dragon.power:.1f}, breath type {dragon.breath}, and {dragon.wins} wins, coming from the house of {dragon.house.name}. Currently participating in {dragon_quests} quests."


def update_dragons_data():
    dragons = Dragon.objects.filter(is_healthy=False, power__gt=1.0)
    dragons_count = dragons.count()

    if dragons_count == 0:
        return "No changes in dragons data."

    for dragon in dragons:
        new_power = max(float(dragon.power) - 0.1, 1.0)
        dragon.power = new_power
        dragon.is_healthy = True
        dragon.save()

    min_power = Dragon.objects.aggregate(Min("power"))["power__min"]
    return f"The data for {dragons_count} dragon/s has been changed. The minimum power level among all dragons is {min_power:.1f}"


def get_earliest_quest():

    quest = Quest.objects.all().order_by("start_time").first()

    if not quest:
        return "No relevant data."

    day = quest.start_time.day
    month = quest.start_time.month
    year = quest.start_time.year

    dragons = quest.dragons.all().order_by("-power", "name")
    dragon_names = "*".join(dragon.name for dragon in dragons)
    avg_power = dragons.aggregate(Avg("power"))["power__avg"]
    return (
        f"The earliest quest is: {quest.name}, "
        f"code: {quest.code}, "
        f"start date: {day}.{month}.{year}, "
        f"host: {quest.host.name}. "
        f"Dragons: {dragon_names}. "
        f"Average dragons power level: {avg_power:.2f}"
    )


def announce_quest_winner(quest_code):
    try:
        quest = Quest.objects.get(code=quest_code)
    except Quest.DoesNotExist:
        return "No such quest."

    winning_dragon = quest.dragons.all().order_by("-power", "name").first()

    if not winning_dragon:
        return "No such quest."

    winning_dragon.wins += 1
    winning_dragon.save()

    winning_house = winning_dragon.house
    winning_house.wins += 1
    winning_house.save()

    dragon_wins = winning_dragon.wins
    house_wins = winning_house.wins
    reward = "{:.2f}".format(quest.reward)

    quest.delete()

    return (
        f"The quest: {quest.name} has been won by dragon {winning_dragon.name} "
        f"from house {winning_house.name}. The number of wins has been updated as follows: "
        f"{dragon_wins} total wins for the dragon and {house_wins} total wins for the house. "
        f"The house was awarded with {reward} coins."
    )
