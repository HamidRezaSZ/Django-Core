from django.db import models
from base.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import User
from django.core.exceptions import ValidationError


class ProductCategory(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children',
                               null=True, blank=True, verbose_name='دسته بندی والد')
    icon = models.FileField(upload_to='product-category-icon', verbose_name='آیکون', null=True, blank=True)

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError('والد باید متفاوت باشد')
        return super().clean()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self) -> str:
        return self.title


class ProductBrand(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children',
                               null=True, blank=True, verbose_name='برند والد')
    icon = models.FileField(upload_to='product-brand-icon', verbose_name='آیکون', null=True, blank=True)

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError('والد باید متفاوت باشد')
        return super().clean()

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self) -> str:
        return self.title


class Product(BaseModel):
    name = models.CharField(max_length=200, verbose_name='نام')
    upc = models.CharField(max_length=200, verbose_name='شناسه محصول')
    image = models.FileField(upload_to='products', verbose_name='عکس شاخص')
    short_description = models.TextField(verbose_name='توضیح مختصر')
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, verbose_name='دسته بندی')
    brand = models.ForeignKey(
        ProductBrand, on_delete=models.CASCADE, verbose_name='برند')
    description = RichTextUploadingField(verbose_name='محتوا')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='کالای پدر')

    def save(self, *args, **kwargs):
        super().save()
        RelatedProduct.objects.get_or_create(product=self)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self) -> str:
        return self.name


class ProductAttribute(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(to=ProductCategory, verbose_name='دسته بندی', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی های محصول'

    def __str__(self) -> str:
        return self.title


class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(
        to=ProductAttribute, verbose_name='دسته بندی ویژگی', on_delete=models.CASCADE)
    value = models.CharField(max_length=200, verbose_name='مقدار')
    products = models.ManyToManyField(to=Product,
                                      verbose_name='محصولات')

    class Meta:
        verbose_name = 'مقدار ویژگی محصول'
        verbose_name_plural = 'مقادیر ویژگی محصول'

    def __str__(self) -> str:
        return f'{self.product_attribute.title} {self.value}'


class ProductComment(models.Model):
    RATE = [(int(x), str(x)) for x in range(1, 6)]

    email = models.EmailField(verbose_name='ایمیل')
    full_name = models.CharField(verbose_name='نام و نام خانوادگی', max_length=200)
    content = models.TextField(verbose_name='متن')
    rate = models.IntegerField(verbose_name='امتیاز', choices=RATE, default=1)
    product = models.ForeignKey(to=Product,
                                verbose_name='محصولات', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='کامنت والد', related_name='child')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    is_accepted = models.BooleanField(default=False, verbose_name='تایید شده')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'کامنت پست'
        verbose_name_plural = 'کامنت های پست'
        ordering = ('created_date',)


class ProductCatalog(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا')
    catalog = models.FileField(upload_to='product-catalogs', verbose_name='کاتالوگ')

    class Meta:
        verbose_name = 'کاتالوگ محصول'
        verbose_name_plural = 'کاتالوگ های محصول'


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا')
    image = models.FileField(verbose_name='عکس')

    class Meta:
        verbose_name = 'عکس محصول'
        verbose_name_plural = 'عکس های محصول'


class RelatedProduct(BaseModel):
    product = models.OneToOneField(to=Product, verbose_name='محصول', on_delete=models.CASCADE)
    related_products = models.ManyToManyField(to=Product, verbose_name='محصولات مرتبط', related_name='related_products')

    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        verbose_name = 'محصول مرتبط'
        verbose_name_plural = 'محصول های مرتبط'


class Seller(BaseModel):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشنده ها'


class ProductQuantity(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا')
    seller = models.ForeignKey(to=Seller, verbose_name='فروشنده', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0, verbose_name='مبلغ')
    quantity = models.PositiveIntegerField(default=0, verbose_name='تعداد')

    def __str__(self):
        return f'{self.product} - ' + "{:,}".format(self.price)

    class Meta:
        verbose_name = 'موجودی کالا'
        verbose_name_plural = 'موجودی های کالا'


class Coupon(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='کاربر مربوطه')
    discount_percent = models.PositiveIntegerField(verbose_name='درصد تخفیف (%):', default=0)
    discount_amount = models.PositiveIntegerField(verbose_name='مبلغ تخفیف (ریال):', default=0)
    discount_code = models.CharField(max_length=200, verbose_name='کد تخفیف')
    expired_date = models.DateField(null=True, verbose_name='تاریخ انقضا')

    def check_user(self, user) -> bool:
        if user != self.user:
            return False
        return True

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'
