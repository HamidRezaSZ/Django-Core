from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin


class ProductCategoryInline(admin.TabularInline):
    model = ProductCategory.product.through
    extra = 1
    max_num = 1


class ProductBrandInline(admin.StackedInline):
    model = ProductBrand.product.through
    extra = 1
    max_num = 1


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 0


class ProductCommentInline(admin.TabularInline):
    model = ProductComment
    extra = 1
    max_num = 1


class RelatedProductInline(admin.TabularInline):
    model = RelatedProduct
    extra = 1
    max_num = 1


class ProductStorageinline(admin.TabularInline):
    model = ProductStorage
    extra = 1
    max_num = 1


class SellerStorageInline(admin.TabularInline):
    model = SellerStorage
    extra = 1
    max_num = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_editable = ('is_active',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_editable = ('is_active',)


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product_type')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'rate', 'created_date', 'is_accepted')
    list_editable = ('is_accepted',)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    inlines = (SellerStorageInline,)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'qty', 'price')


@admin.register(Product)
class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'upc', 'product_type')
    inlines = (ProductCategoryInline, ProductBrandInline,
               ProductAttributeValueInline, ProductCommentInline, RelatedProductInline, ProductStorageinline)


# @admin.register(Coupon)
# class CouponAdmin(admin.ModelAdmin):
#     list_display = ('id', 'discount_percent', 'discount_amount', 'discount_code', 'expired_date')
#     search_fields = ('id', 'discount_code')
