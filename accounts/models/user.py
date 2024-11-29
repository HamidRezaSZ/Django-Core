from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.utils.validators import cell_phone_validator, validate_national_code


class User(AbstractUser):
    GENDER_CHOICES = ((_("Female"), _("Female")), (_("Male"), _("Male")))

    cell_phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=_("cell_phone"),
        validators=[cell_phone_validator],
    )
    avatar = models.ImageField(
        upload_to="user-avatars", verbose_name=_("avatar"), default=""
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=None,
        blank=True,
        null=True,
        verbose_name=_("gender"),
        max_length=10,
    )
    national_id = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name=_("national_id"),
        validators=[validate_national_code],
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    def full_name(self) -> str:
        return "{0} {1}".format(self.first_name, self.last_name)
