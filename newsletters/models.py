from django.db import models
from django.utils.translation import gettext_lazy as _


class NewsLetters(models.Model):
    """
    Get email of user for register to newsletters
    """

    email = models.EmailField(unique=True, verbose_name=_('email'))

    class Meta:
        verbose_name = _('NewsLetters')
        verbose_name_plural = _('NewsLetters')
