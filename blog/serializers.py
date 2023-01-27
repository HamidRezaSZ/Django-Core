from rest_framework import serializers
from blog.models import *


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('parent',)


class PostCategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = ('parent',)

    def get_sub_categories(self, obj):
        return SubCategorySerializer(obj.children.all(), many=True).data


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('parent', 'user')


class PostCommentSerializer(serializers.ModelSerializer):
    sub_comments = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    galleries = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ('parent', 'is_accepted')
        read_only_fields = ('is_accepted',)
        extra_kwargs = {
            'email': {'write_only': True},
        }

    def get_sub_comments(self, obj):
        return SubCommentSerializer(obj.child.all(), many=True).data

    def get_authors(self, obj):
        return AuthorSerializer(obj.author_set.all(), many=True).data

    def get_tags(self, obj):
        return TagSerializer(obj.gallery_set.all(), many=True).data

    def get_galleries(self, obj):
        return GallerySerializer(obj.gallery_set.all(), many=True).data


class PostSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'description', 'show_in_home_page', 'thumbnail', 'created_date')


class PostItemSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class RelatedPostSerializer(serializers.ModelSerializer):
    related_post = PostSerializer(many=True)

    class Meta:
        model = RelatedPost
        fields = '__all__'
