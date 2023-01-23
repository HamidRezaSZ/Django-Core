from rest_framework import serializers
from .models import *
from django.db.models import Avg


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class SubBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    sub_brands = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = '__all__'

    def get_sub_brands(self, obj):
        return SubBrandSerializer(obj.children.filter(is_active=True), many=True).data


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_sub_categories(self, obj):
        return SubCategorySerializer(obj.children.filter(is_active=True), many=True).data


class ProductSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_score(self, obj):
        return ProductComment.objects.get(product=obj).comment.aggregate(Avg('rate'))['rate__avg']


class SubProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    storages = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_score(self, obj):
        return ProductComment.objects.get(product=obj).comment.aggregate(Avg('rate'))['rate__avg']

    def get_brand(self, obj):
        return BrandSerializer(ProductBrand.objects.get(product=obj).brand).data

    def get_category(self, obj):
        return CategorySerializer(ProductCategory.objects.get(product=obj).category).data

    def get_attributes(self, obj):
        return ProductAttributeValueSerializer(obj.productattributevalue_set.all(), many=True).data

    def get_storages(self, obj):
        return StorageSerializer(
            ProductStorage.objects.filter(product=obj).values_list('storage', flat=True),
            many=True).data


class ProductItemSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    sub_products = serializers.SerializerMethodField()
    storages = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_score(self, obj):
        return ProductComment.objects.get(product=obj).comment.aggregate(Avg('rate'))['rate__avg']

    def get_brand(self, obj):
        return BrandSerializer(ProductBrand.objects.get(product=obj).brand).data

    def get_category(self, obj):
        return CategorySerializer(ProductCategory.objects.get(product=obj).category).data

    def get_attributes(self, obj):
        return ProductAttributeValueSerializer(obj.productattributevalue_set.all(), many=True).data

    def get_sub_products(self, obj):
        return SubProductSerializer(obj.child.all(), many=True).data

    def get_storages(self, obj):
        return StorageSerializer(
            ProductStorage.objects.filter(product=obj).values_list('storage', flat=True),
            many=True).data


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    product_attribute = ProductAttributeSerializer()

    class Meta:
        model = ProductAttributeValue
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductCommentSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)

    class Meta:
        model = ProductComment
        fields = '__all__'


class RelatedProductSerializer(serializers.ModelSerializer):
    related_product = ProductSerializer(many=True)

    class Meta:
        model = RelatedProduct
        fields = '__all__'


class CreateProductCommentSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.filter(is_active=True))

    class Meta:
        model = ProductComment
        exclude = ('is_active',)

    def create(self, validated_data):
        product_comment_obj = ProductComment.objects.get(post=validated_data['product'])
        product_comment_obj.comment.add(Comment.objects.create(**validated_data['comment']))
        return product_comment_obj


class SellerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.username


class StorageSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()

    class Meta:
        model = Storage
        fields = '__all__'

    def get_seller(self, obj):
        return SellerSerializer(SellerStorage.objects.get(storage=obj)).data

# class ProductCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCategory
#         exclude = ('parent',)


# class ProductCategoryGetSerializer(serializers.ModelSerializer):
#     sub_categories = serializers.SerializerMethodField()

#     class Meta:
#         model = ProductCategory
#         exclude = ('parent',)

#     def get_sub_categories(self, obj):
#         return ProductCategorySerializer(obj.children, many=True, read_only=True).data


# class AllProductsSerializer(serializers.ModelSerializer):
#     scores = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = ('name', 'short_description', 'image', 'scores')

#     def get_scores(self, obj):
#         return obj.review_set.aggregate(Avg('score'))


# class ProductAttributeSerializer(serializers.ModelSerializer):
#     related_product = AllProductsSerializer()

#     class Meta:
#         model = ProductAttribute
#         exclude = ('related_product',)


# class ProductQuantitySerializer(serializers.ModelSerializer):
#     related_product_attribute = ProductAttributeSerializer()

#     class Meta:
#         model = ProductQuantity
#         exclude = ('related_product',)


# class ProductCatalogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCatalog
#         exclude = ('related_product',)


# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         exclude = ('related_product',)


# class ProductItemSerializer(serializers.ModelSerializer):
#     related_product_category = ProductCategorySerializer()
#     product_attribute = serializers.SerializerMethodField()
#     product_quantity = serializers.SerializerMethodField()
#     catalogs = serializers.SerializerMethodField()
#     scores = serializers.SerializerMethodField()
#     related_products = AllProductsSerializer(many=True)
#     images = serializers.SerializerMethodField()

#     class Meta:
#         model = Product
#         fields = '__all__'

#     def get_product_attribute(self, obj):
#         return ProductAttributeSerializer(obj.productattribute_set.all(), many=True).data

#     def get_product_quantity(self, obj):
#         return ProductQuantitySerializer(obj.productquantity_set.all(), many=True).data

#     def get_catalogs(self, obj):
#         return ProductCatalogSerializer(obj.productcatalog_set.all(), many=True).data

#     def get_images(self, obj):
#         return ProductImageSerializer(obj.productimage_set.all(), many=True).data

#     def get_scores(self, obj):
#         return obj.review_set.filter(is_accepted=True).aggregate(Avg('score'))


# class CouponSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coupon
#         exclude = ('related_product_category', 'related_product')


# class ReviewProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         exclude = ('related_product', 'is_accepted')
#         extra_kwargs = {
#             'related_user': {'write_only': True},
#         }


# class ReviewProductGetSerializer(serializers.ModelSerializer):
#     sub_comments = serializers.SerializerMethodField()

#     class Meta:
#         model = Review
#         exclude = ('related_product', 'is_accepted', 'related_user')

#     def create(self, validated_data):
#         user = self.context.get('user')
#         validated_data['related_user'] = user
#         return super().create(validated_data)

#     def get_sub_comments(self, obj):
#         return ReviewProductSerializer(obj.children.filter(is_accepted=True), many=True, read_only=True).data
