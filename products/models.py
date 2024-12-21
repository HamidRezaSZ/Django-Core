from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from base.models.base_model import BaseModel


class ProductCategory(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    slug = models.SlugField(unique=True, verbose_name=_("title"))
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
        blank=True,
        verbose_name=_("parent"),
    )
    icon = models.FileField(
        upload_to="product-category-icon", verbose_name=_("icon"), null=True, blank=True
    )
    image_alt = models.CharField(max_length=200, verbose_name=_("image_alt"))
    description = RichTextUploadingField(
        verbose_name=_("description"), null=True, blank=True
    )
    meta_title = models.CharField(
        max_length=128, verbose_name=_("meta_title"), null=True, blank=True
    )
    meta_description = models.TextField(
        verbose_name=_("meta_description"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.title

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError("parent must be different")
        return super().clean()


class ProductBrand(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        null=True,
        blank=True,
        verbose_name=_("parent"),
    )
    icon = models.FileField(
        upload_to="product-brand-icon", verbose_name=_("icon"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self) -> str:
        return self.title

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError("parent must be different")
        return super().clean()


class Product(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    slug = models.SlugField(unique=True, verbose_name=_("slug"))
    upc = models.CharField(max_length=200, verbose_name=_("upc"))
    image = models.FileField(upload_to="products", verbose_name=_("image"))
    image_alt = models.CharField(max_length=200, verbose_name=_("image_alt"))
    short_description = models.TextField(verbose_name=_("short_description"))
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, verbose_name=_("category")
    )
    brand = models.ForeignKey(
        ProductBrand, on_delete=models.CASCADE, verbose_name=_("brand")
    )
    description = RichTextUploadingField(verbose_name=_("description"))
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("parent"),
    )
    meta_title = models.CharField(
        max_length=128, verbose_name=_("meta_title"), null=True, blank=True
    )
    meta_description = models.TextField(
        verbose_name=_("meta_description"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self) -> str:
        return self.name


class ProductAttribute(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    category = models.ForeignKey(
        to=ProductCategory, verbose_name=_("category"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Attribute")
        verbose_name_plural = _("Attributes")

    def __str__(self) -> str:
        return self.title


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(
        to=ProductAttribute,
        verbose_name=_("product_attribute"),
        on_delete=models.CASCADE,
    )
    value = models.CharField(max_length=200, verbose_name=_("value"))
    products = models.ManyToManyField(to=Product, verbose_name=_("products"))

    class Meta:
        verbose_name = _("Attribute Value")
        verbose_name_plural = _("Attribute Values")

    def __str__(self) -> str:
        return f"{self.product_attribute.title} {self.value}"


class ProductComment(models.Model):
    RATE = [(int(x), str(x)) for x in range(1, 6)]

    email = models.EmailField(verbose_name=_("email"))
    full_name = models.CharField(verbose_name=_("full_name"), max_length=200)
    content = models.TextField(verbose_name=_("content"))
    rate = models.IntegerField(verbose_name=_("rate"), choices=RATE, default=1)
    product = models.ForeignKey(
        to=Product, verbose_name=_("product"), on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("parent"),
        related_name="child",
    )
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created_date")
    )
    is_accepted = models.BooleanField(default=False, verbose_name=_("is_accepted"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ("created_date",)

    def __str__(self) -> str:
        return self.email


class ProductCatalog(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("product")
    )
    catalog = models.FileField(upload_to="product-catalogs", verbose_name=_("catalog"))

    class Meta:
        verbose_name = _("Catalog")
        verbose_name_plural = _("Catalogs")


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("product")
    )
    image = models.FileField(verbose_name=_("image"))

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class ProductTag(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("product")
    )
    tag = models.CharField(max_length=50, verbose_name=_("tag"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class RelatedProduct(BaseModel):
    product = models.OneToOneField(
        to=Product, verbose_name=_("product"), on_delete=models.CASCADE
    )
    related_products = models.ManyToManyField(
        to=Product, verbose_name=_("related_products"), related_name="related_products"
    )

    class Meta:
        verbose_name = _("Related Product")
        verbose_name_plural = _("Related Products")

    def __str__(self) -> str:
        return f"{self.product.name}"


class Seller(BaseModel):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, verbose_name=_("user")
    )

    class Meta:
        verbose_name = _("Seller")
        verbose_name_plural = _("Sellers")

    def __str__(self) -> str:
        return f"{self.user.username}"


class ProductQuantity(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("product")
    )
    seller = models.ForeignKey(
        to=Seller, verbose_name=_("seller"), on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_("quantity"))

    class Meta:
        verbose_name = _("Product Quantity")
        verbose_name_plural = _("Product Quantities")

    def __str__(self) -> str:
        return f"{self.product} - " + "{:,}".format(self.price)


class Coupon(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name=_("user")
    )
    discount_percent = models.PositiveIntegerField(
        verbose_name=_("discount_percent"), default=0
    )
    discount_amount = models.PositiveIntegerField(
        verbose_name=_("discount_amount"), default=0
    )
    discount_code = models.CharField(max_length=200, verbose_name=_("discount_code"))
    expired_date = models.DateField(null=True, verbose_name=_("expired_date"))

    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def check_user(self, user) -> bool:
        if user != self.user:
            return False
        return True
