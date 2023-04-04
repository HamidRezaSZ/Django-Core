from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))

    def __str__(self):
        return self.user.username

    def get_cart_price(self):
        return sum([item.get_cart_item_price() for item in self.cartitem_set.all()])

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, verbose_name=_('cart'), on_delete=models.CASCADE)
    product_quantity = models.ForeignKey(
        'products.ProductQuantity', on_delete=models.PROTECT, verbose_name=_('product_quantity'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('quantity'))

    def __str__(self):
        return f'{self.product_quantity}'

    def get_cart_item_price(self):
        return self.product_quantity.price * self.quantity

    def save(self, *args, **kwargs):
        if self.product_quantity.quantity < self.quantity:
            raise ValueError('The item is unavailable')
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')
