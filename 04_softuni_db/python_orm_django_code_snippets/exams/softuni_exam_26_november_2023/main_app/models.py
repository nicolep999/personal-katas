from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from main_app.mixins import PublishedOnMixin, ContentMixin
from main_app.managers import AuthorManager

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2005)]
    )
    website = models.URLField(null=True, blank=True)

    objects = AuthorManager()


class Article(PublishedOnMixin, ContentMixin):

    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = "Technology"
        SCIENCE = "Science"
        EDUCATION = "Education"

    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.TECHNOLOGY,
    )
    authors = models.ManyToManyField(Author)


class Review(PublishedOnMixin, ContentMixin):
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
