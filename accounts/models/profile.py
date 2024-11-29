from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    MARITAL_STATUS = ((_("Single"), _("Single")), (_("Married"), _("Married")))

    user = models.OneToOneField(
        verbose_name=_("user"), to="accounts.User", on_delete=models.CASCADE
    )
    day_of_birth = models.DateField(_("day_of_birth"), null=True, blank=True)
    marital_status = models.CharField(
        _("marital_status"),
        max_length=10,
        choices=MARITAL_STATUS,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        to="base.City",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("city"),
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self) -> str:
        return self.user.cell_phone
