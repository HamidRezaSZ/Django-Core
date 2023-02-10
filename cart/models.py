from django.db import models
from accounts.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        product_count = self.cartitem_set.count()
        return '{} کالا توسط {}'.format(product_count, self.user.username)

    def get_cart_price(self):
        return sum([item.get_cart_item_price() for item in self.cartitem_set.all()])

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, verbose_name='سبد خرید ', on_delete=models.CASCADE)
    product_quantity = models.ForeignKey(
        'products.ProductQuantity', on_delete=models.PROTECT, verbose_name='کالا')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return f'{self.product_quantity}'

    def get_cart_item_price(self):
        return self.product_quantity.price * self.quantity

    def save(self, *args, **kwargs):
        if self.product_quantity.quantity < self.quantity:
            raise ValueError('The item is unavailable')
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'کالای سبد خرید'
        verbose_name_plural = 'کالا های سبد خرید'
