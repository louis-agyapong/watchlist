from django.db import models
from django.utils.translation import gettext_lazy as _
from core.common.models import BaseModel, SoftDeleteModel


class StreamingPlatform(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    about = models.TextField(_("About"), blank=True)
    website = models.URLField(_("Website"), max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name


class Movie(SoftDeleteModel):
    title = models.CharField(_("Title"), max_length=100)
    platform = models.ForeignKey(
        StreamingPlatform,
        verbose_name=_("Platform"),
        on_delete=models.SET_NULL,
        related_name="movies",
        blank=True,
        null=True,
    )
    plot = models.TextField(_("Story Line"), blank=True)
    active = models.BooleanField(_("Active"), default=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    def __str__(self) -> str:
        return self.title
