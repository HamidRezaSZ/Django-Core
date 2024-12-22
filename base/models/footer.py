from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.singleton import SingletonModel
from base.models.base_model import BaseModel


class FooterColumn(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    link = models.CharField(
        verbose_name=_("link"), null=True, blank=True, max_length=500
    )
    order = models.IntegerField(default=1, verbose_name=_("order"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Footer Column")
        verbose_name_plural = _("Footer Columns")
        ordering = ("order",)


class FooterRow(BaseModel):
    footer_column = models.ForeignKey(
        to=FooterColumn,
        verbose_name=_("footer_column"),
        on_delete=models.CASCADE,
        related_name="rows",
    )
    title = models.CharField(max_length=200, verbose_name=_("title"))
    link = models.CharField(verbose_name=_("link"), max_length=500)
    order = models.IntegerField(default=1, verbose_name=_("order"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Footer Row")
        verbose_name_plural = _("Footer Rows")
        ordering = ("order",)


class Footer(SingletonModel):
    logo = models.FileField(upload_to="footer", verbose_name=_("logo"))
    text = models.TextField(verbose_name=_("text"))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("Footer")
        verbose_name_plural = _("Footer")


class FooterImage(BaseModel):
    image = models.FileField(upload_to="footer-images", verbose_name=_("image"))
    link = models.CharField(
        verbose_name=_("link"), null=True, blank=True, max_length=500
    )
    order = models.IntegerField(default=1, verbose_name=_("order"))

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = _("Footer Image")
        verbose_name_plural = _("Footer Images")
        ordering = ("order",)
