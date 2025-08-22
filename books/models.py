from django.db import models
from django.contrib.auth import settings

class Author(models.Model):
    full_name = models.CharField(max_length=255)
    country = models.CharField(max_length=63, blank=True, null=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BookListing(models.Model):
    class ConditionChoices(models.TextChoices):
        NEW = "new", "New"
        EXCELLENT = "excellent", "Excellent quality"
        GOOD = "good", "Good quality"
        FAIR = "fair", "Normal quality"
        POOR = "poor", "Bad quality"

    title = models.CharField(max_length=255)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="books/covers/"
    )
    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        related_name="books",
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="owned_books",
        on_delete=models.CASCADE
    )
    condition = models.CharField(
        max_length=20,
        choices=ConditionChoices.choices,
        default=ConditionChoices.GOOD
    )
    description = models.TextField(max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.author.full_name} {self.genre.name})"
