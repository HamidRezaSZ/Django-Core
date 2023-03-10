from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from accounts.validators import cell_phone_validator
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        abstract = True


class FAQ(BaseModel):
    question = models.CharField(verbose_name='سوال', max_length=500)
    answer = models.TextField(verbose_name='جواب')

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'


class AboutUs(BaseModel):
    text = RichTextUploadingField(verbose_name='محتوا')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class ContactUsForm(models.Model):
    full_name = models.CharField(verbose_name='نام و نام خانوادگی', max_length=200)
    cell_phone_number = models.CharField(
        _('شماره موبایل'),
        max_length=11, validators=[cell_phone_validator])
    message = models.TextField(verbose_name='پیام')

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'فرم تماس با ما'
        verbose_name_plural = 'فرم تماس با ما'


class SocialAccount(BaseModel):
    link = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='social_accounts')

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'


class ContactUsDetail(BaseModel):
    image = models.ImageField(verbose_name='عکس', upload_to='contact_us')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(verbose_name='شماره تلفن', max_length=20)
    social_accounts = models.ManyToManyField(verbose_name='شبکه های اجتماعی', to=SocialAccount)

    class Meta:
        verbose_name = 'صفحه تماس با ما'
        verbose_name_plural = 'صفحه تماس با ما'


class Page(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')
    link = models.CharField(max_length=500, verbose_name='لینک')

    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحه ها'

    def __str__(self) -> str:
        return self.title


class Menu(BaseModel):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE, verbose_name='صفحه')
    icon = models.FileField(null=True, blank=True, upload_to='menus', verbose_name='آیکون')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               blank=True, null=True, related_name='children', verbose_name='والد')
    order = models.IntegerField(default=1, verbose_name='ترتیب نمایش')

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError('والد باید متفاوت باشد')
        return super().clean()

    def __str__(self):
        full_path = [self.page.title]
        k = self.parent
        while k is not None:
            full_path.append(k.page.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name = 'منو'
        verbose_name_plural = 'منو ها'
        ordering = ('order',)


class Slider(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')
    text = models.TextField(verbose_name='متن')
    link = models.CharField(max_length=500, null=True, blank=True, verbose_name='لینک')
    image = models.FileField(upload_to='slider', verbose_name='عکس')
    order = models.IntegerField(default=1, verbose_name='اولویت نمایش')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'
        ordering = ('order',)

    def __str__(self) -> str:
        return self.title


class Footer(BaseModel):
    logo = models.FileField(upload_to='footer', verbose_name='لوگو')
    content = models.TextField(verbose_name='محتوا')
    useful_link = models.ManyToManyField(Page, verbose_name='صفحه ها')
    social_accounts = models.ManyToManyField(SocialAccount, verbose_name='شبکه های اجتماعی')
    contact_us = models.ForeignKey(ContactUsDetail, on_delete=models.CASCADE, verbose_name='تماس با ما')

    class Meta:
        verbose_name = 'فوتر'
        verbose_name_plural = 'فوتر'


class State(BaseModel):
    name = models.CharField(max_length=200, verbose_name='نام')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'
        ordering = ['name']


class City(BaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='استان مربوطه')
    name = models.CharField(max_length=256, verbose_name='نام')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'
        ordering = ['name']


class TermsAndConditions(BaseModel):
    text = RichTextUploadingField(verbose_name='محتوا')

    class Meta:
        verbose_name = 'قوانین و مقررات'
        verbose_name_plural = 'قوانین و مقررات'


class Component(BaseModel):
    name = models.CharField(verbose_name='نام', max_length=200)
    page = models.ManyToManyField(to=Page, verbose_name='صفحه')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               blank=True, null=True, related_name='children', verbose_name='والد')
    order = models.IntegerField(default=1, verbose_name='اولویت نمایش')

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError('والد باید متفاوت باشد')
        return super().clean()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'کامپوننت'
        verbose_name_plural = 'کامپوننت ها'
        ordering = ['order']


class ComponentItem(BaseModel):
    class Type(models.TextChoices):
        FILE = 'File', 'File'
        TEXT = 'Text', 'Text'

    component = models.ForeignKey(to=Component, on_delete=models.CASCADE, verbose_name='کامپوننت')
    type = models.CharField(verbose_name='نوع', max_length=20, choices=Type.choices)
    file = models.FileField(verbose_name='فایل', upload_to='component', null=True, blank=True)
    content = RichTextUploadingField(verbose_name='محتوا', null=True, blank=True)

    def clean(self) -> None:
        if self.type == 'File' and (not self.file or self.content):
            raise ValidationError('نوع کامپوننت فایل است!')
        elif self.type == 'Text' and (self.file or not self.content):
            raise ValidationError('نوع کامپوننت متن است!')
        return super().clean()

    class Meta:
        verbose_name = 'بخش کامپوننت'
        verbose_name_plural = 'بخش های کامپوننت'
