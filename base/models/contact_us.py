from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.utils.validators import cell_phone_validator
from base.models.singleton import SingletonModel
from base.models.social_account import SocialAccount


class ContactUsForm(models.Model):
    full_name = models.CharField(verbose_name=_("full_name"), max_length=200)
    cell_phone_number = models.CharField(
        _("cell_phone_number"), max_length=11, validators=[cell_phone_validator]
    )
    message = models.TextField(verbose_name=_("message"))

    class Meta:
        verbose_name = _("Contact Us Form")
        verbose_name_plural = _("Contact Us Forms")

    def __str__(self) -> str:
        return self.full_name


class ContactUsDetail(SingletonModel):
    image = models.FileField(verbose_name=_("image"), upload_to="contact_us")
    email = models.EmailField(verbose_name=_("email"))
    phone_number = models.CharField(verbose_name=_("phone_number"), max_length=20)
    social_accounts = models.ManyToManyField(
        verbose_name=_("social_accounts"), to=SocialAccount
    )

    class Meta:
        verbose_name = _("Contact Us Detail")
        verbose_name_plural = _("Contact Us Detail")
