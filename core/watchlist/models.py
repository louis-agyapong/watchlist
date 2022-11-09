from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    """
    An individual
    """

    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} + {self.last_name}"


class Genre(models.Model):
    """
    Movie Genre
    """

    name = models.CharField(_("Name"), max_length=255)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    class MovieType(models.TextChoices):
        MOVIE: str = "movie", _("MOVIE")
        SERIES: str = "series", _("SERIES")
        EPISODE: str = "EPISODE", _("EPISODE")

    title = models.CharField(_("Title"), max_length=50)
    release_year = models.DateField(_("Release Year"), blank=True, null=True)
    type = models.CharField(_("Type"), max_length=50)
    genre = models.ManyToManyField(Genre, verbose_name=_("Genre"), blank=True)
    description = models.TextField(_("Description"), blank=True, default="")
    active = models.BooleanField(_("Active"), default=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self) -> str:
        return self.name
