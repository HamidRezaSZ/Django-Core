from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'blog'

router = DefaultRouter()

router.register(r'posts', PostView)
router.register(r'categories', CategoryView)
router.register(r'comments', CommentView)
router.register(r'related-posts', RelatedPostView)

urlpatterns = router.urls
