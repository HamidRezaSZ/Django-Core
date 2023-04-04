from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from base.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'), related_name='children')

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError('parent must be different')
        return super().clean()

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Author(BaseModel):
    user = models.OneToOneField(to=User, verbose_name=_('user'), on_delete=models.CASCADE)
    about = models.CharField(verbose_name=_('about'), max_length=200)
    avatar = models.FileField(verbose_name=_('avatar'))
    avatar_alt = models.CharField(max_length=200, verbose_name=_('avatar_alt'))

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Post(BaseModel):
    title = models.CharField(max_length=256, verbose_name=_('title'))
    slug = models.SlugField(unique=True, verbose_name=_('slug'))
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name=_('category'))
    thumbnail = models.ImageField(upload_to='post-images', verbose_name=_('thumbnail'))
    image_alt = models.CharField(max_length=200, verbose_name=_('image_alt'))
    description = models.TextField(verbose_name=_('description'))
    content = RichTextUploadingField(verbose_name=_('content'))
    authors = models.ManyToManyField(to=Author, verbose_name=_('authors'))
    show_in_home_page = models.BooleanField(default=False, verbose_name=_('show_in_home_page'))
    meta_title = models.CharField(max_length=128, verbose_name=_('meta_title'), null=True, blank=True)
    meta_description = models.TextField(verbose_name=_('meta_description'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-created_date',)


class Gallery(BaseModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name=_('post'))
    image = models.FileField(verbose_name=_('image'))
    image_alt = models.CharField(verbose_name=_('image_alt'), max_length=200)

    def __str__(self):
        return f'{self.image.url}'

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')


class Tag(BaseModel):
    title = models.CharField(verbose_name=_('title'), max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name=_('post'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Comment(models.Model):
    RATE = [(int(x), str(x)) for x in range(1, 6)]

    email = models.EmailField(verbose_name=_('email'))
    full_name = models.CharField(verbose_name=_('full_name'), max_length=200)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name=_('post'))
    content = models.TextField(verbose_name=_('content'))
    rate = models.IntegerField(verbose_name=_('rate'), choices=RATE, default=1)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'), related_name='child')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created_date'))
    is_accepted = models.BooleanField(default=False, verbose_name=_('is_accepted'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('created_date',)


class RelatedPost(models.Model):
    post = models.OneToOneField(
        to=Post, verbose_name=_('post'),
        on_delete=models.CASCADE, related_name='related_post_post')
    related_posts = models.ManyToManyField(to=Post, verbose_name=_('related_posts'), null=True)

    def __str__(self):
        return f'{self.post.title}'

    class Meta:
        verbose_name = _('Related Post')
        verbose_name_plural = _('Related Posts')
