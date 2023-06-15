from django.db.models import Avg
from rest_framework import serializers

from base.base_serializers import *

from .models import *


class ProductBrandSerializer(ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = ProductBrand
        fields = '__all__'


class ProductCategorySerializer(ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'upc', 'image', 'short_description', 'category', 'brand', 'score')

    def get_score(self, obj):
        return obj.productcomment_set.filter(is_accepted=True).aggregate(Avg('rate'))['rate__avg'] or 0


class SubProductSerializer(ModelSerializer):
    category = ProductCategorySerializer()
    brand = ProductBrandSerializer()
    score = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    catelogs = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('parent',)

    def get_score(self, obj):
        return obj.productcomment_set.filter(is_accepted=True).aggregate(Avg('rate'))['rate__avg'] or 0

    def get_attributes(self, obj):
        return ProductAttributeValueSerializer(obj.productattributevalue_set.all(), many=True).data

    def get_catelogs(self, obj):
        return ProductCatalogSerializer(obj.productcatalog_set.all(), many=True).data

    def get_images(self, obj):
        return ProductImageSerializer(obj.productimage_set.all(), many=True).data

    def get_quantities(self, obj):
        return ProductQuantitiesSerializer(obj.productquantity_set.all(), many=True).data

    def get_tags(self, obj):
        return ProductTagSerializer(obj.producttag_set.all(), many=True).data


class ProductItemSerializer(ModelSerializer):
    category = ProductCategorySerializer()
    brand = ProductBrandSerializer()
    score = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    catelogs = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    quantities = serializers.SerializerMethodField()
    sub_products = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('parent',)

    def get_score(self, obj):
        return obj.productcomment_set.filter(is_accepted=True).aggregate(Avg('rate'))['rate__avg'] or 0

    def get_attributes(self, obj):
        return ProductAttributeValueSerializer(obj.productattributevalue_set.all(), many=True).data

    def get_catelogs(self, obj):
        return ProductCatalogSerializer(obj.productcatalog_set.all(), many=True).data

    def get_images(self, obj):
        return ProductImageSerializer(obj.productimage_set.all(), many=True).data

    def get_quantities(self, obj):
        return ProductQuantitiesSerializer(obj.productquantity_set.all(), many=True).data

    def get_sub_products(self, obj):
        return SubProductSerializer(obj.child.all(), many=True).data

    def get_tags(self, obj):
        return ProductTagSerializer(obj.producttag_set.all(), many=True).data


class ProductAttributeSerializer(ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductAttributeValueSerializer(ModelSerializer):
    product_attribute = ProductAttributeSerializer()

    class Meta:
        model = ProductAttributeValue
        fields = '__all__'


class RelatedProductSerializer(ModelSerializer):
    related_products = ProductSerializer(many=True)

    class Meta:
        model = RelatedProduct
        fields = '__all__'


class SellerSerializer(ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username


class ProductCatalogSerializer(ModelSerializer):
    class Meta:
        model = ProductCatalog
        exclude = ('product',)


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('product',)


class ProductTagSerializer(ModelSerializer):
    class Meta:
        model = ProductTag
        exclude = ('product',)


class ProductQuantitiesSerializer(ModelSerializer):

    class Meta:
        model = ProductQuantity
        fields = '__all__'


class ProductCommentSerializer(ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = ProductComment
        exclude = ('is_accepted',)
        extra_kwargs = {
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user
        return super().create(validated_data)
