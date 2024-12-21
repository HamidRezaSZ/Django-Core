from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel
from base.models.page import Page


class Menu(BaseModel):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE, verbose_name=_("page"))
    icon = models.FileField(
        null=True, blank=True, upload_to="menus", verbose_name=_("icon")
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
        verbose_name=_("parent"),
    )
    order = models.IntegerField(default=1, verbose_name=_("order"))

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")
        ordering = ("order",)

    def __str__(self) -> str:
        full_path = [self.page.title]
        k = self.parent
        while k is not None:
            full_path.append(k.page.title)
            k = k.parent
        return " -> ".join(full_path[::-1])

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError("parent must be different")
        return super().clean()
