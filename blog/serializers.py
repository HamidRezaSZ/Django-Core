from rest_framework import serializers

from base.base_serializers import ModelSerializer
from blog.models import *


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('is_active', 'created_date', 'modified_date', 'parent')


class PostCategorySerializer(ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = ('is_active', 'created_date', 'modified_date', 'parent')

    def get_sub_categories(self, obj):
        return SubCategorySerializer(obj.children.all(), many=True).data


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Author
        exclude = ('is_active', 'created_date', 'modified_date', 'user')

    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


class SubCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('parent', 'user')


class PostCommentSerializer(ModelSerializer):
    sub_comments = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ('parent', 'is_accepted')
        read_only_fields = ('is_accepted',)
        extra_kwargs = {
            'email': {'write_only': True},
        }

    def get_sub_comments(self, obj):
        return SubCommentSerializer(obj.child.all(), many=True).data


class PostSerializer(ModelSerializer):
    category = PostCategorySerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'description', 'show_in_home_page', 'thumbnail', 'created_date')


class PostItemSerializer(ModelSerializer):
    category = PostCategorySerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Post
        exclude = ('is_active',)


class RelatedPostSerializer(ModelSerializer):
    related_posts = PostSerializer(many=True)

    class Meta:
        model = RelatedPost
        fields = '__all__'
