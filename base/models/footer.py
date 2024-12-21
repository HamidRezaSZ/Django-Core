from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel
from base.models.contact_us import ContactUsDetail
from base.models.page import Page
from base.models.social_account import SocialAccount


class Footer(BaseModel):
    logo = models.FileField(upload_to="footer", verbose_name=_("logo"))
    content = models.TextField(verbose_name=_("content"))
    useful_link = models.ManyToManyField(Page, verbose_name=_("useful_link"))
    social_accounts = models.ManyToManyField(
        SocialAccount, verbose_name=_("social_accounts")
    )
    contact_us = models.ForeignKey(
        ContactUsDetail, on_delete=models.CASCADE, verbose_name=_("contact_us")
    )

    class Meta:
        verbose_name = _("Footer")
        verbose_name_plural = _("Footers")
