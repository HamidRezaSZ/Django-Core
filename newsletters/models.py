from django.db import models


class NewsLetters(models.Model):
    """
    Get email of user for register to newsletters
    """

    email = models.EmailField(unique=True, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'خبرنامه'
        verbose_name_plural = 'خبرنامه'
