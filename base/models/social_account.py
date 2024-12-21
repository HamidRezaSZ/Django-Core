from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel


class SocialAccount(BaseModel):
    link = models.CharField(max_length=500, verbose_name=_("link"))
    logo = models.FileField(upload_to="social_accounts", verbose_name=_("logo"))

    class Meta:
        verbose_name = _("Social Account")
        verbose_name_plural = _("Social Accounts")
