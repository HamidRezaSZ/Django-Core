from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import Page
from base.models.base_model import BaseModel
from base.models.page import Page


class Slider(BaseModel):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE, verbose_name=_("page"))
    title = models.CharField(max_length=200, verbose_name=_("title"))
    text = models.TextField(verbose_name=_("text"))
    link = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_("link")
    )
    image = models.FileField(upload_to="slider", verbose_name=_("image"))
    order = models.IntegerField(default=1, verbose_name=_("order"))

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")
        ordering = ("order",)

    def __str__(self) -> str:
        return self.title
