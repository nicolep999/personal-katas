import os
import django
from django.db.models import Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review

# Create queries within functions


def get_authors(search_name=None, search_email=None):
    authors = Author.objects.all()

    if search_name is not None and search_email is not None:
        authors = authors.filter(
            full_name__icontains=search_name, email__icontains=search_email
        )
    elif search_name is not None:
        authors = authors.filter(full_name__icontains=search_name)
    elif search_email is not None:
        authors = authors.filter(email__icontains=search_email)
    else:
        return ""

    if not authors.exists():
        return ""

    authors = authors.order_by("-full_name")

    result = []
    for author in authors:
        status = "Banned" if author.is_banned else "Not Banned"
        result.append(
            f"Author: {author.full_name}, email: {author.email}, status: {status}"
        )

    return "\n".join(result)


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    if (
        not top_author
        or not hasattr(top_author, "article_count")
        or top_author.article_count == 0
    ):
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.article_count} published articles."


def get_top_reviewer():
    top_reviewer = (
        Author.objects.annotate(review_count=Count("review"))
        .order_by("-review_count", "email")
        .first()
    )

    if (
        not top_reviewer
        or not hasattr(top_reviewer, "review_count")
        or top_reviewer.review_count == 0
    ):
        return ""

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.review_count} published reviews."


def get_latest_article():
    latest_article = Article.objects.order_by("-published_on").first()

    if not latest_article:
        return ""

    authors = latest_article.authors.all().order_by("full_name")
    author_names = ", ".join([author.full_name for author in authors])

    reviews_info = Review.objects.filter(article=latest_article).aggregate(
        num_reviews=Count("id"), avg_rating=Avg("rating")
    )

    num_reviews = reviews_info["num_reviews"] or 0
    avg_rating = reviews_info["avg_rating"] or 0

    return (
        f"The latest article is: {latest_article.title}. "
        f"Authors: {author_names}. "
        f"Reviewed: {num_reviews} times. "
        f"Average Rating: {avg_rating:.2f}."
    )


def get_top_rated_article():
    top_article = (
        Article.objects.annotate(
            avg_rating=Avg("review__rating"), num_reviews=Count("review")
        )
        .filter(num_reviews__gt=0)
        .order_by("-avg_rating", "title")
        .first()
    )

    if not top_article or not top_article.num_reviews:
        return ""

    return (
        f"The top-rated article is: {top_article.title}, "
        f"with an average rating of {top_article.avg_rating:.2f}, "
        f"reviewed {top_article.num_reviews} times."
    )


def ban_author(email=None):
    if not email:
        return "No authors banned."

    try:
        author = Author.objects.get(email=email)
    except Author.DoesNotExist:
        return "No authors banned."

    num_reviews = author.review_set.count()
    author.review_set.all().delete()

    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."
