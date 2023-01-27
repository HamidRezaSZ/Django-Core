from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'products'

router = DefaultRouter()

router.register(r'products', ProductsView)
router.register(r'categories', ProductCategoryView)
router.register(r'brands', ProductBrandView)
router.register(r'product-comments', ProductCommentView)
router.register(r'related-products', RelatedProductView)

urlpatterns = router.urls
