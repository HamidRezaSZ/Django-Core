from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel


class State(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("name"))

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class City(BaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_("state"))
    name = models.CharField(max_length=256, verbose_name=_("name"))

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        ordering = ["name"]

    def __str__(self):
        return self.name
