from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.utils.validators import cell_phone_validator


class Address(models.Model):
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, verbose_name=_("user")
    )
    first_name = models.CharField(max_length=200, verbose_name=_("first_name"))
    last_name = models.CharField(max_length=200, verbose_name=_("last_name"))
    phone_number = models.CharField(max_length=20, verbose_name=_("phone_number"))
    telephone_number = models.CharField(
        max_length=20,
        verbose_name=_("telephone_number"),
        validators=[cell_phone_validator],
    )
    email = models.EmailField(verbose_name=_("email"))
    address = models.TextField(verbose_name=_("address"))
    zip_code = models.CharField(max_length=30, verbose_name=_("zip_code"))
    city = models.ForeignKey(
        to="base.City", on_delete=models.PROTECT, verbose_name=_("city")
    )
    description = models.TextField(verbose_name=_("description"), null=True, blank=True)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return self.user.username
