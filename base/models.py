from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.validators import cell_phone_validator


class BaseModel(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created_date'))
    modified_date = models.DateTimeField(
        auto_now=True, verbose_name=_('modified_date'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))

    class Meta:
        abstract = True


class FAQ(BaseModel):
    question = models.CharField(verbose_name=_('question'), max_length=500)
    answer = models.TextField(verbose_name=_('answer'))

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self) -> str:
        return self.question


class AboutUs(BaseModel):
    text = RichTextUploadingField(verbose_name=_('text'))

    class Meta:
        verbose_name = _('About Us')
        verbose_name_plural = _('About Us')


class ContactUsForm(models.Model):
    full_name = models.CharField(verbose_name=_('full_name'), max_length=200)
    cell_phone_number = models.CharField(
        _('cell_phone_number'),
        max_length=11, validators=[cell_phone_validator])
    message = models.TextField(verbose_name=_('message'))

    class Meta:
        verbose_name = _('Contact Us Form')
        verbose_name_plural = _('Contact Us Forms')

    def __str__(self) -> str:
        return self.full_name


class SocialAccount(BaseModel):
    link = models.CharField(max_length=500, verbose_name=_('link'))
    logo = models.FileField(
        upload_to='social_accounts', verbose_name=_('logo'))

    class Meta:
        verbose_name = _('Social Account')
        verbose_name_plural = _('Social Accounts')


class ContactUsDetail(BaseModel):
    image = models.FileField(verbose_name=_('image'), upload_to='contact_us')
    email = models.EmailField(verbose_name=_('email'))
    phone_number = models.CharField(
        verbose_name=_('phone_number'), max_length=20)
    social_accounts = models.ManyToManyField(
        verbose_name=_('social_accounts'), to=SocialAccount)

    class Meta:
        verbose_name = _('Contact Us Detail')
        verbose_name_plural = _('Contact Us Detail')


class Page(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    link = models.CharField(max_length=500, verbose_name=_('link'))

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')

    def __str__(self) -> str:
        return self.title


class Menu(BaseModel):
    page = models.ForeignKey(
        to=Page, on_delete=models.CASCADE, verbose_name=_('page'))
    icon = models.FileField(null=True, blank=True,
                            upload_to='menus', verbose_name=_('icon'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               blank=True, null=True, related_name='children', verbose_name=_('parent'))
    order = models.IntegerField(default=1, verbose_name=_('order'))

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')
        ordering = ('order',)

    def __str__(self) -> str:
        full_path = [self.page.title]
        k = self.parent
        while k is not None:
            full_path.append(k.page.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError('parent must be different')
        return super().clean()


class Slider(BaseModel):
    page = models.ForeignKey(
        to=Page, on_delete=models.CASCADE, verbose_name=_('page'))
    title = models.CharField(max_length=200, verbose_name=_('title'))
    text = models.TextField(verbose_name=_('text'))
    link = models.CharField(max_length=500, null=True,
                            blank=True, verbose_name=_('link'))
    image = models.FileField(upload_to='slider', verbose_name=_('image'))
    order = models.IntegerField(default=1, verbose_name=_('order'))

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')
        ordering = ('order',)

    def __str__(self) -> str:
        return self.title


class Footer(BaseModel):
    logo = models.FileField(upload_to='footer', verbose_name=_('logo'))
    content = models.TextField(verbose_name=_('content'))
    useful_link = models.ManyToManyField(Page, verbose_name=_('useful_link'))
    social_accounts = models.ManyToManyField(
        SocialAccount, verbose_name=_('social_accounts'))
    contact_us = models.ForeignKey(
        ContactUsDetail, on_delete=models.CASCADE, verbose_name=_('contact_us'))

    class Meta:
        verbose_name = _('Footer')
        verbose_name_plural = _('Footers')


class State(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('name'))

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class City(BaseModel):
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, verbose_name=_('state'))
    name = models.CharField(max_length=256, verbose_name=_('name'))

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        ordering = ['name']

    def __str__(self):
        return self.name


class TermsAndConditions(BaseModel):
    text = RichTextUploadingField(verbose_name=_('text'))

    class Meta:
        verbose_name = _('Terms And Conditions')
        verbose_name_plural = _('Terms And Conditions')


class DynamicText(BaseModel):
    key = models.CharField(max_length=200, unique=True, verbose_name=_('key'))
    value = models.TextField(verbose_name=_('value'))

    class Meta:
        verbose_name = _('Dynamic Text')
        verbose_name_plural = _('Dynamic Texts')

    def __str__(self) -> str:
        return self.key
