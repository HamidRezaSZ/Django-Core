from django.db import models
from accounts.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        product_count = self.cartitem_set.count()
        return '{} کالا توسط {}'.format(product_count, self.user.username)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, verbose_name='سبد خرید ', on_delete=models.CASCADE)
    product_quantity = models.ForeignKey(
        'products.Product', on_delete=models.PROTECT, verbose_name='کالا')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return f'{self.product_quantity}'

    def get_price(self):
        return self.product_quantity.price * self.quantity

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'
