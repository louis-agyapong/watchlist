from django.core.checks.messages import Error
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
    all_objects = models.Manager()  # default manager

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore_delete(self):
        self.is_deleted = False
        self.save()

    def delete(self):
        raise Error()

    class Meta:
        abstract = True
