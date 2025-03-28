from main_app.models import models


class AuthorManager(models.Manager):

    def get_authors_by_article_count(self):
        return self.annotate(article_count=models.Count("article")).order_by(
            "-article_count", "email"
        )
