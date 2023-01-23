from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .validators import validate_national_code


class User(AbstractUser):
    GENDER_CHOICES = (
        ('Female', 'خانم'),
        ('Male', 'آقا')
    )

    cell_phone_validator = RegexValidator(
        regex=r'^(09|9)\d{9}$',
        message='Start with 09/9 and it must 9 digits after that. For example: 0912000000 or 912000000000')
    cell_phone = models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')
    avatar = models.ImageField(upload_to='user-avatars', verbose_name='آواتار', default='')
    gender = models.CharField(choices=GENDER_CHOICES, default=None, blank=True,
                              null=True, verbose_name='جنسیت', max_length=10)
    national_id = models.CharField(max_length=10, blank=True, null=True,
                                   verbose_name='کد ملی', validators=[validate_national_code])

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Address(models.Model):
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')
    first_name = models.CharField(max_length=200, verbose_name='نام')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=20, verbose_name='تلفن ثابت')
    telephone_number = models.CharField(max_length=20, verbose_name='تلفن همراه')
    email = models.EmailField(verbose_name='ایمیل')
    address = models.TextField(verbose_name='آدرس')
    zip_code = models.CharField(max_length=30, verbose_name='کد پستی')
    related_city = models.ForeignKey(to='base.City', on_delete=models.PROTECT, verbose_name='شهر')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self) -> str:
        return self.related_user.username

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'


class Profile(models.Model):
    class MaritalStatus(models.TextChoices):
        MALE = 'Single', 'مجرد'
        MARRIED = 'Married', 'متاهل'

    related_user = models.ForeignKey(verbose_name=('کاربر'), to=User, on_delete=models.CASCADE)
    day_of_birth = models.DateField(_('تاریخ تولد'), null=True, blank=True)
    marital_status = models.CharField(_('وضعیت تاهل'), max_length=10,
                                      choices=MaritalStatus.choices, null=True, blank=True)
    related_city = models.ForeignKey(to='base.City', on_delete=models.SET_NULL,
                                     blank=True, null=True, verbose_name='شهر مربوطه')

    def __str__(self) -> str:
        return self.related_user.cell_phone

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل'
