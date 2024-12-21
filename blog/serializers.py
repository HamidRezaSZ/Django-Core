from rest_framework import serializers

from base.serializers.base_serializers import *
from blog.models import *


class PostCategorySerializer(ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        exclude = ('is_active', 'created_date', 'modified_date', 'parent')


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


class PostCommentSerializer(ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Comment
        exclude = ('parent', 'is_accepted')
        read_only_fields = ('is_accepted',)
        extra_kwargs = {
            'email': {'write_only': True},
        }


class PostSerializer(ModelSerializer):
    category = PostCategorySerializer()
    created_date = serializers.DateTimeField(format="%Y/%m/%d", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'description',
                  'show_in_home_page', 'thumbnail', 'created_date')


class PostItemSerializer(ModelSerializer):
    category = PostCategorySerializer()
    authors = AuthorSerializer(many=True)
    tags = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField(format="%Y/%m/%d", read_only=True)

    class Meta:
        model = Post
        exclude = ('is_active',)

    def get_tags(self, obj):
        return TagSerializer(obj.tag_set.filter(is_active=True), many=True).data


class RelatedPostSerializer(ModelSerializer):
    related_posts = PostSerializer(many=True)

    class Meta:
        model = RelatedPost
        fields = '__all__'
