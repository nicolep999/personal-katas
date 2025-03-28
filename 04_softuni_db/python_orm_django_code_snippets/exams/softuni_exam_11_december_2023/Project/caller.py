import os
import django
from django.db.models import Q, Count
from django.db.models.expressions import result

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions
def get_tennis_players(search_name=None, search_country=None) -> str:
    tennis_players = TennisPlayer.objects.all()

    if search_name is not None and search_country is not None:
        tennis_players = tennis_players.filter(
            Q(full_name__icontains=search_name) & Q(country__icontains=search_country)
        )
    elif search_name is not None:
        tennis_players = tennis_players.filter(Q(full_name__icontains=search_name))
    elif search_country is not None:
        tennis_players = tennis_players.filter(Q(country__icontains=search_country))
    else:
        return ""

    tennis_players = tennis_players.order_by("ranking")

    if not tennis_players:
        return ""

    result = [
        f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}"
        for player in tennis_players
    ]
    return "\n".join(result)


def get_top_tennis_player():
    top_tennis_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not top_tennis_player:
        return ""

    return f"Top Tennis Player: {top_tennis_player.full_name} with {top_tennis_player.total_wins} wins."


def get_tennis_player_by_matches_count():
    player = (
        TennisPlayer.objects.annotate(total_matches=Count("match"))
        .order_by("-total_matches", "ranking")
        .first()
    )

    if not player or not player.total_matches:
        return ""

    return (
        f"Tennis Player: {player.full_name} with {player.total_matches} matches played."
    )


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    tournaments = (
        Tournament.objects.filter(surface_type__icontains=surface)
        .annotate(num_matches=Count("match"))
        .order_by("-start_date")
    )

    if not tournaments:
        return ""

    result = [
        f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}"
        for t in tournaments
    ]
    return "\n".join(result)


def get_latest_match_info():
    match = Match.objects.order_by("-date_played", "-id").first()

    if not match:
        return ""

    players = match.players.order_by("full_name")
    player_names = " vs ".join([p.full_name for p in players])
    winner = match.winner.full_name if match.winner else "TBA"

    return f"Latest match played on: {match.date_played}, tournament: {match.tournament.name}, score: {match.score}, players: {player_names}, winner: {winner}, summary: {match.summary}"


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    try:
        tournament = Tournament.objects.get(name=tournament_name)
    except Tournament.DoesNotExist:
        return "No matches found."

    matches = tournament.match_set.order_by("-date_played")

    if not matches:
        return "No matches found."

    result = []
    for match in matches:
        winner = match.winner.full_name if match.winner else "TBA"
        result.append(
            f"Match played on: {match.date_played}, score: {match.score}, winner: {winner}"
        )

    return "\n".join(result)
