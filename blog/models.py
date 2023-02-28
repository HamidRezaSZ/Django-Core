from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import User
from base.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی والد', related_name='children')

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError('والد باید متفاوت باشد')
        return super().clean()

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Author(BaseModel):
    user = models.OneToOneField(to=User, verbose_name='کاربر', on_delete=models.CASCADE)
    about = models.CharField(verbose_name='درباره من', max_length=200)
    avater = models.FileField(verbose_name='آواتار')
    avater_alt = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'


class Post(BaseModel):
    title = models.CharField(max_length=256, verbose_name='عنوان')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    thumbnail = models.ImageField(upload_to='post-images', verbose_name='تصویر شاخص')
    description = models.TextField(verbose_name='توضیحات مختصر')
    content = RichTextUploadingField(verbose_name='محتوای پست')
    authors = models.ManyToManyField(to=Author, verbose_name='نویسنده ها')
    show_in_home_page = models.BooleanField(default=False, verbose_name='نمایش در صفحه اصلی')
    meta_title = models.CharField(max_length=128, verbose_name='عنوان سئو', null=True, blank=True)
    meta_description = models.TextField(verbose_name='توضیحات سئو', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save()
        RelatedPost.objects.get_or_create(post=self)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ('-created_date',)


class Gallery(BaseModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name='پست')
    image = models.FileField(verbose_name='عکس')
    image_alt = models.CharField(verbose_name='alt', max_length=200)

    def __str__(self):
        return f'{self.image.url}'

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'


class Tag(BaseModel):
    title = models.CharField(verbose_name='تایتل', max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name='پست')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Comment(models.Model):
    RATE = [(int(x), str(x)) for x in range(1, 6)]

    email = models.EmailField(verbose_name='ایمیل')
    full_name = models.CharField(verbose_name='نام و نام خانوادگی', max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name='پست')
    content = models.TextField(verbose_name='متن')
    rate = models.IntegerField(verbose_name='امتیاز', choices=RATE, default=1)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='کامنت والد', related_name='child')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    is_accepted = models.BooleanField(default=False, verbose_name='تایید شده')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'کامنت پست'
        verbose_name_plural = 'کامنت های پست'
        ordering = ('created_date',)


class RelatedPost(models.Model):
    post = models.OneToOneField(to=Post, verbose_name='پست', on_delete=models.CASCADE, related_name='related_post_post')
    related_posts = models.ManyToManyField(to=Post, verbose_name='پست', null=True)

    def __str__(self):
        return f'{self.post.title}'

    class Meta:
        verbose_name = 'پست مرتبط'
        verbose_name_plural = 'پست های مرتبط'
