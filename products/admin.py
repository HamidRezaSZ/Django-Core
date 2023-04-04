from django.contrib import admin
from import_export.admin import ImportExportMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import *


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
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ProductBrand)
class ProductBrandAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_editable = ('is_active',)


@admin.register(ProductAttribute)
class ProductAttributeAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'category')
    search_fields = ('title',)


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(TranslationAdmin):
    list_display = ('id', 'product_attribute', 'value')
    search_fields = ('value',)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


class ProductCatalogInline(admin.TabularInline):
    model = ProductCatalog
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductTagnline(TranslationTabularInline):
    model = ProductTag
    extra = 0


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 0


@admin.register(Product)
class ProductAdmin(ImportExportMixin, TranslationAdmin):
    list_display = ('id', 'category', 'brand', 'name', 'upc', 'parent', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('id', 'description', 'short_description', 'name', 'upc')
    prepopulated_fields = {"slug": ("name",)}
    inlines = (ProductAttributeValueInline, ProductCommentInline,
               RelatedProductInline, ProductCatalogInline, ProductImageInline, ProductQuantityInline, ProductTagnline)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'discount_percent', 'discount_amount', 'discount_code', 'expired_date', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('id', 'discount_code')
