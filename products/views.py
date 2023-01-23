from base.viewsets import ModelViewSet
from .serializers import *
from .models import *
from .filters import ProductFilter
from rest_framework.permissions import IsAdminUser, AllowAny


class ProductsView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Product.objects.filter(is_active=True, parent=None)
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductItemSerializer

        return ProductSerializer


class CategoryView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Category.objects.filter(is_active=True, parent=None)
    serializer_class = CategorySerializer


class BrandView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Brand.objects.filter(is_active=True, parent=None)
    serializer_class = BrandSerializer


class ProductTypeView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ProductType.objects.filter(is_active=True)
    serializer_class = ProductTypeSerializer


class ProductCommentView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ProductComment.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProductCommentSerializer

        return ProductCommentSerializer

    filterset_fields = ['comment', 'product']


class RelatedProductView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = RelatedProduct.objects.filter(is_active=True)
    serializer_class = RelatedProductSerializer
    filterset_fields = ['related_product', 'product']
