import django_filters
from django_filters import FilterSet
from .models import Product, ProductCategory, ProductBrand


class ProductFilter(FilterSet):
    productcategory = django_filters.ModelChoiceFilter(
        label='postcategory', queryset=ProductCategory.objects.filter(is_active=True))
    productbrand = django_filters.ModelChoiceFilter(
        label='productbrand', queryset=ProductBrand.objects.filter(is_active=True))

    class Meta:
        model = Product
        fields = ['product_type', 'parent', 'productcategory', 'productbrand']
