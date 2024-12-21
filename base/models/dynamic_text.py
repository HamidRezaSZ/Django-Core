from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel


class DynamicText(BaseModel):
    key = models.CharField(max_length=200, unique=True, verbose_name=_("key"))
    value = models.TextField(verbose_name=_("value"))

    class Meta:
        verbose_name = _("Dynamic Text")
        verbose_name_plural = _("Dynamic Texts")

    def __str__(self) -> str:
        return self.key
