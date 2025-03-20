import os
from decimal import Decimal

import django
from django.db.models.functions import Least

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Director, Movie
from django.db.models import Q, Count, Avg, F


# Create queries within functions


def populate_db():
    actor1 = Actor.objects.create(
        full_name="Tom Cruise", birth_date="1976-07-03", nationality="American"
    )

    actor2 = Actor.objects.create(
        full_name="Robert Downey Jr.", birth_date="1965-04-04", nationality="American"
    )

    actor3 = Actor.objects.create(
        full_name="Chris Evans", birth_date="1981-06-13", nationality="American"
    )

    director1 = Director.objects.create(
        full_name="James Cameron", birth_date="1954-08-16", nationality="American"
    )

    director2 = Director.objects.create(
        full_name="Akira Kurosawa", birth_date="1910-03-23", nationality="Japanese"
    )

    director3 = Director.objects.create(
        full_name="Martin Scorsese", birth_date="1942-11-17", nationality="American"
    )

    movie1 = Movie.objects.create(
        title="Avatar",
        release_date="2009-12-10",
        director=director1,
        storyline="A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        is_awarded=True,
        is_classic=True,
        genre="Action",
        rating=7.9,
        starring_actor=actor1,
    )

    movie1.actors.add(actor2, actor3)

    movie2 = Movie.objects.create(
        title="The Dark Knight",
        release_date="2008-07-18",
        director=director2,
        storyline="A superhero who fights crime as a masked vigilante in Gotham City.",
        is_awarded=True,
        is_classic=False,
        genre="Action",
        rating=9.0,
        starring_actor=actor2,
    )
    movie2.actors.add(actor1, actor3)


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query = Q()
    if search_name is not None:
        query &= Q(full_name__icontains=search_name)
    if search_nationality is not None:
        query &= Q(nationality__icontains=search_nationality)

    directors = Director.objects.filter(query).order_by("full_name")

    if not directors.exists():
        return ""

    result = []
    for director in directors:
        result.append(
            f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}"
        )

    return "\n".join(result)


def get_top_director():

    director = Director.objects.get_directors_by_movies_count().first()

    if not director or not director.director_movies.exists():
        return ""

    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    top_actor = (
        Actor.objects.annotate(num_of_movies=Count("starring_movies"))
        .order_by("-num_of_movies", "full_name")
        .first()
    )
    if not top_actor or not top_actor.starring_movies.exists():
        return ""

    movies = top_actor.starring_movies.all()
    movie_titles = ", ".join([movie.title for movie in movies])
    avg_rating = movies.aggregate(Avg("rating"))["rating__avg"]

    return f"Top Actor: {top_actor.full_name}, starring in movies: {movie_titles}, movies average rating: {avg_rating:.1f}"


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(
        num_movies=Count("starring_movies", distinct=True)
        + Count("actor_movies", distinct=True)
    ).filter(num_movies__gt=0)

    actors = actors.order_by("-num_movies", "full_name")[:3]

    if not actors:
        return ""

    return "\n".join(
        f"{actor.full_name}, participated in {actor.num_movies} movies"
        for actor in actors
    )


def get_top_rated_awarded_movie():
    movie = Movie.objects.filter(is_awarded=True).order_by("-rating", "title").first()

    if not movie:
        return ""

    return f"Top rated awarded movie: {movie.title}, rating: {movie.rating:.1f}. Starring actor: {movie.starring_actor.full_name if movie.starring_actor else 'N/A'}. Cast: {', '.join([actor.full_name for actor in movie.actors.all()])}."


def increase_rating():
    updated_count = Movie.objects.filter(is_classic=True, rating__lt=10).update(
        rating=Least(F("rating") + 0.1, 10.0)
    )

    return (
        f"Rating increased for {updated_count} movies."
        if updated_count
        else "No ratings increased."
    )
