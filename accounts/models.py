from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import cell_phone_validator, validate_national_code


class User(AbstractUser):
    GENDER_CHOICES = (
        (_('Female'), _('Female')),
        (_('Male'), _('Male'))
    )

    cell_phone = models.CharField(max_length=11, unique=True, verbose_name=_('cell_phone'),
                                  validators=[cell_phone_validator])
    avatar = models.ImageField(upload_to='user-avatars', verbose_name=_('avatar'), default='')
    gender = models.CharField(choices=GENDER_CHOICES, default=None, blank=True,
                              null=True, verbose_name=_('gender'), max_length=10)
    national_id = models.CharField(max_length=10, blank=True, null=True,
                                   verbose_name=_('national_id'), validators=[validate_national_code])

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    first_name = models.CharField(max_length=200, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=200, verbose_name=_('last_name'))
    phone_number = models.CharField(max_length=20, verbose_name=_('phone_number'))
    telephone_number = models.CharField(
        max_length=20, verbose_name=_('telephone_number'),
        validators=[cell_phone_validator])
    email = models.EmailField(verbose_name=_('email'))
    address = models.TextField(verbose_name=_('address'))
    zip_code = models.CharField(max_length=30, verbose_name=_('zip_code'))
    city = models.ForeignKey(to='base.City', on_delete=models.PROTECT, verbose_name=_('city'))
    description = models.TextField(verbose_name=_('description'))

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class Profile(models.Model):
    MARITAL_STATUS = (
        (_('Single'), _('Single')),
        (_('Married'), _('Married'))
    )

    user = models.OneToOneField(verbose_name=_('user'), to=User, on_delete=models.CASCADE)
    day_of_birth = models.DateField(_('day_of_birth'), null=True, blank=True)
    marital_status = models.CharField(_('marital_status'), max_length=10,
                                      choices=MARITAL_STATUS, null=True, blank=True)
    city = models.ForeignKey(to='base.City', on_delete=models.SET_NULL,
                             blank=True, null=True, verbose_name=_('city'))

    def __str__(self) -> str:
        return self.user.cell_phone

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
