from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True
