from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import *


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0


class TagInline(TranslationTabularInline):
    model = Tag
    extra = 0


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class RelatedPostInline(admin.TabularInline):
    model = RelatedPost
    filter_horizontal = ('related_posts',)


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('id', 'category', 'title', 'created_date', 'show_in_home_page', 'is_active')
    list_filter = ('category',)
    filter_horizontal = ('authors',)
    list_editable = ('show_in_home_page', 'is_active')
    inlines = (GalleryInline, TagInline, RelatedPostInline, CommentInline)
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    search_fields = ('title',)
    list_editable = ('is_active',)


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    list_display = ('id', 'user', 'about', 'is_active')
    search_fields = ('about', 'image', 'image_alt')
    list_editable = ('is_active',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Comment.objects.filter(parent=None)

    list_display = ('id', 'post', 'email', 'full_name', 'rate', 'parent', 'created_date', 'is_accepted')
    list_editable = ('is_accepted',)
    list_filter = ('post',)
    search_fields = ('email', 'full_name', 'content')
    inlines = [
        CommentInline
    ]
