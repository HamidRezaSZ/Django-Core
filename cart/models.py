from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self) -> str:
        return self.user.username

    def get_cart_price(self) -> int:
        return sum([item.get_cart_item_price() for item in self.cartitem_set.all()])


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, verbose_name=_('cart'), on_delete=models.CASCADE)
    product_quantity = models.ForeignKey(
        'products.ProductQuantity', on_delete=models.PROTECT, verbose_name=_('product_quantity'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('quantity'))

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')

    def __str__(self) -> str:
        return f'{self.product_quantity}'

    def save(self, *args, **kwargs) -> None:
        if self.product_quantity.quantity < self.quantity:
            raise ValidationError('The item is unavailable')
        return super().save(*args, **kwargs)

    def get_cart_item_price(self) -> int:
        return self.product_quantity.price * self.quantity
