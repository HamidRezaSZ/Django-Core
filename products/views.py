from base.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser, AllowAny


class ProductsView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Product.objects.filter(is_active=True, parent=None)
    filterset_fields = ['category', 'brand', 'parent']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductItemSerializer

        return ProductSerializer


class ProductCategoryView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ProductCategory.objects.filter(is_active=True, parent=None)
    serializer_class = ProductCategorySerializer
    filterset_fields = ['parent']


class ProductBrandView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ProductBrand.objects.filter(is_active=True, parent=None)
    serializer_class = ProductBrandSerializer


class ProductCommentView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ProductComment.objects.filter(is_accepted=True, parent=None)
    serializer_class = ProductCommentSerializer
    filterset_fields = ['parent', 'is_accepted', 'rate']


class RelatedProductView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = RelatedProduct.objects.filter(is_active=True)
    serializer_class = RelatedProductSerializer
    filterset_fields = ['related_products', 'product']
