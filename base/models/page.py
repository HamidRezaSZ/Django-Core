from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel


class Page(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    link = models.CharField(max_length=500, verbose_name=_("link"))

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self) -> str:
        return self.title
