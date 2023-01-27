from rest_framework import serializers
from .models import *
from django.db.models import Avg


class SubProductBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductBrand
        fields = '__all__'


class ProductBrandSerializer(serializers.ModelSerializer):
    sub_brands = serializers.SerializerMethodField()

    class Meta:
        model = ProductBrand
        fields = '__all__'

    def get_sub_brands(self, obj):
        return SubProductBrandSerializer(obj.children.filter(is_active=True), many=True).data


class SubProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = '__all__'

    def get_sub_categories(self, obj):
        return SubProductCategorySerializer(obj.children.filter(is_active=True), many=True).data


class ProductSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'upc', 'image', 'short_description', 'category', 'brand')

    def get_score(self, obj):
        return ProductComment.objects.get(product=obj).comment.aggregate(Avg('rate'))['rate__avg']


class SubProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    brand = ProductBrandSerializer()
    score = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    catelogs = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('parent',)

    def get_score(self, obj):
        return ProductComment.objects.get(product=obj).comment.aggregate(Avg('rate'))['rate__avg']

    def get_attributes(self, obj):
        return ProductAttributeValueSerializer(obj.productattributevalue_set.all(), many=True).data

    def get_catelogs(self, obj):
        return ProductCatalogSerializer(obj.productcatalog_set.all(), many=True).data

    def get_images(self, obj):
        return ProductImageSerializer(obj.productimage_set.all(), many=True).data

    def get_quantities(self, obj):
        return ProductQuantitiesSerializer(obj.productquantity_set.all(), many=True).data


class ProductItemSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    brand = ProductBrandSerializer()
    score = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    catelogs = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    quantities = serializers.SerializerMethodField()
    sub_products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('parent',)

    def get_score(self, obj):
        return ProductComment.objects.get(product=obj).comment.aggregate(Avg('rate'))['rate__avg']

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


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    product_attribute = ProductAttributeSerializer()

    class Meta:
        model = ProductAttributeValue
        fields = '__all__'


class RelatedProductSerializer(serializers.ModelSerializer):
    related_products = ProductSerializer(many=True)

    class Meta:
        model = RelatedProduct
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username


class ProductCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatalog
        exclude = ('product',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('product',)


class ProductQuantitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuantity
        fields = '__all__'


class SubProductCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductComment
        exclude = ('product', 'is_accepted')
        extra_kwargs = {
            'email': {'write_only': True},
        }


class ProductCommentSerializer(serializers.ModelSerializer):
    sub_comments = serializers.SerializerMethodField()

    class Meta:
        model = ProductComment
        exclude = ('product', 'is_accepted')
        extra_kwargs = {
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user
        return super().create(validated_data)

    def get_sub_comments(self, obj):
        return SubProductCommentSerializer(obj.children.filter(is_accepted=True), many=True, read_only=True).data
