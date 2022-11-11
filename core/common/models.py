from django.db import models
from django.utils.translation import gettext as _
from .managers import SoftDeleteManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(_("Is Deleted"), default=True)
    objects = SoftDeleteManager()


    class Meta:
        abstract = True
