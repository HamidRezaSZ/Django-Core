from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel
from cart.models import Cart
from payments.models import Payment


class DeliveryType(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    delivery_price = models.PositiveIntegerField(default=0, verbose_name=_('delivery_price'))

    class Meta:
        verbose_name = _('Delivery Type')
        verbose_name_plural = _('Delivery Types')

    def __str__(self) -> str:
        return self.title


class OrderStatus(BaseModel):
    status = models.CharField(max_length=200, verbose_name=_('status'))

    class Meta:
        verbose_name = _('Order Status')
        verbose_name_plural = _('Order Statuses')

    def __str__(self) -> str:
        return self.status


class Order(models.Model):
    user = models.ForeignKey(to='accounts.User', on_delete=models.CASCADE, verbose_name=_('user'))
    address = models.ForeignKey('accounts.Address', on_delete=models.PROTECT, verbose_name=_('address'))
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.PROTECT, verbose_name=_('delivery_type'))
    payment = models.ForeignKey(
        'payments.Payment', on_delete=models.PROTECT, blank=True, null=True, verbose_name=_('payment'))
    coupon_code = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('coupon_code'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    discount_amount = models.PositiveIntegerField(default=0, verbose_name=_('discount_amount'))
    status = models.ForeignKey(to=OrderStatus, on_delete=models.CASCADE, verbose_name=_('status'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def save(self, *args, **kwargs) -> None:
        cart_obj = Cart.objects.get(user=self.user)
        self.price = cart_obj.get_cart_price() + self.delivery_type.delivery_price
        payment_obj = Payment.objects.create(user=self.user, amount=self.price-self.discount_amount)
        self.payment = payment_obj
        super().save()
        for item in cart_obj.cartitem_set.all():
            OrderItem.objects.create(order=self, product_quantity=item.product_quantity, quantity=item.quantity)
        cart_obj.cartitem_set.filter().delete()

    def get_order_price(self) -> int:
        return sum([item.get_order_item_price() for item in self.orderitem_set.all()])


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, verbose_name=_('order'), on_delete=models.CASCADE)
    product_quantity = models.ForeignKey(
        'products.ProductQuantity', on_delete=models.PROTECT, verbose_name=_('product_quantity'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('quantity'))

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    def __str__(self) -> str:
        return f'{self.product_quantity}'

    def get_order_item_price(self) -> int:
        return self.product_quantity.price * self.quantity
