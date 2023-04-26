# Generated by Django 4.1.3 on 2023-04-04 09:55

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_post_image_alt_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_date',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_date',), 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='relatedpost',
            options={'verbose_name': 'Related Post', 'verbose_name_plural': 'Related Posts'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.CharField(max_length=200, verbose_name='about'),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.FileField(upload_to='', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar_alt',
            field=models.CharField(max_length=200, verbose_name='avatar_alt'),
        ),
        migrations.AlterField(
            model_name='author',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='author',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='author',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.category', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='is_accepted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='blog.comment', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='rate'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.FileField(upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_alt',
            field=models.CharField(max_length=200, verbose_name='image_alt'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ManyToManyField(to='blog.author', verbose_name='authors'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_alt',
            field=models.CharField(max_length=200, verbose_name='image_alt'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta_description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='meta_title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='meta_title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='show_in_home_page',
            field=models.BooleanField(default=False, verbose_name='show_in_home_page'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='post-images', verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=256, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='relatedpost',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_post_post', to='blog.post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='relatedpost',
            name='related_posts',
            field=models.ManyToManyField(null=True, to='blog.post', verbose_name='related_posts'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
    ]