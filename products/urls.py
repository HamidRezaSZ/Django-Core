from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'products'

router = DefaultRouter()

router.register(r'products', ProductsView)
router.register(r'categories', CategoryView)
router.register(r'brands', BrandView)
router.register(r'product-types', ProductTypeView)
router.register(r'product-comments', ProductCommentView)
router.register(r'related-products', RelatedProductView)

urlpatterns = router.urls
