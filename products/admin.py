from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue.products.through
    extra = 0


class ProductCommentInline(admin.TabularInline):
    model = ProductComment
    extra = 0


class RelatedProductInline(admin.TabularInline):
    model = RelatedProduct
    extra = 0


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_editable = ('is_active',)


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_editable = ('is_active',)


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_attribute', 'value')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


class ProductCatalogInline(admin.TabularInline):
    model = ProductCatalog
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 0


@admin.register(Product)
class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'category', 'brand', 'name', 'upc', 'parent', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('id', 'description', 'short_description', 'name', 'upc')
    inlines = (ProductAttributeValueInline, ProductCommentInline,
               RelatedProductInline, ProductCatalogInline, ProductImageInline, ProductQuantityInline)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'discount_percent', 'discount_amount', 'discount_code', 'expired_date', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('id', 'discount_code')