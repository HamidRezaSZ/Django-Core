from .models import *
from .serializers import *
from base.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser


class PostView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Post.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostItemSerializer

        return PostSerializer

    filterset_fields = ['category', 'show_in_home_page']
    search_fields = ['title', 'description', 'content']


class CategoryView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Category.objects.filter(is_active=True, parent=None)
    serializer_class = PostCategorySerializer
    filterset_fields = ['title', 'parent']
    search_fields = ['title']


class CommentView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [AllowAny],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Comment.objects.filter(is_accepted=True, parent=None)
    serializer_class = PostCommentSerializer
    filterset_fields = ['post', 'rate']


class RelatedPostView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = RelatedPost.objects.all()
    serializer_class = RelatedPostSerializer
    filterset_fields = ['post']
