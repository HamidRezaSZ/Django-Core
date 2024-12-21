from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created_date'))
    modified_date = models.DateTimeField(
        auto_now=True, verbose_name=_('modified_date'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))

    class Meta:
        abstract = True