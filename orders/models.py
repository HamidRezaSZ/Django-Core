from django.db import models
from base.models import BaseModel
from payments.models import Payment
from cart.models import Cart


class DeliveryType(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')
    description = models.TextField(verbose_name='توضیحات')
    delivery_price = models.PositiveIntegerField(default=0, verbose_name='هزینه ارسال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نوع ارسال'
        verbose_name_plural = 'انواع ارسال'


class Order(models.Model):
    class Staus(models.TextChoices):
        AWAITING_PAYMENT = 'درانتظار پرداخت', 'درانتظار پرداخت'
        PAID = 'پرداخت شده', 'پرداخت شده'
        SENT = 'ارسال شده', 'ارسال شده'

    user = models.ForeignKey(to='accounts.User', on_delete=models.CASCADE, verbose_name='کاربر')
    address = models.ForeignKey('accounts.Address', on_delete=models.PROTECT, verbose_name='آدرس')
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.PROTECT, verbose_name='نوع ارسال')
    payment = models.ForeignKey(
        'payments.Payment', on_delete=models.PROTECT, blank=True, null=True, verbose_name='پرداخت')
    coupon_code = models.CharField(max_length=200, blank=True, null=True, verbose_name='کد تخفیف')
    price = models.PositiveIntegerField(default=0, verbose_name='مبلغ')
    descounted_price = models.PositiveIntegerField(default=0, verbose_name='مبلغ بعد از تخفیف')
    discount_amount = models.PositiveIntegerField(default=0, verbose_name='مبلغ تخفیف')
    status = models.CharField(choices=Staus.choices, max_length=20, default='درانتظار پرداخت', verbose_name='وضعیت')

    def save(self, *args, **kwargs) -> None:
        super().save()
        cart_obj = Cart.objects.get(related_user=self.user)
        for item in cart_obj.cartitem_set.all():
            OrderItem.objects.create(order=self, product_quantity=item.product_quantity, quantity=item.quantity)
        cart_obj.cartitem_set.delete()
        payment_obj = Payment.objects.create(user=self.user, amount=self.price)
        self.payment = payment_obj

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, verbose_name='سفارش', on_delete=models.CASCADE)
    product_quantity = models.ForeignKey(
        'products.Product', on_delete=models.PROTECT, verbose_name='کالا')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return f'{self.product_quantity}'

    def get_price(self):
        return self.product_quantity.price * self.quantity

    class Meta:
        verbose_name = 'کالای سفارش'
        verbose_name_plural = 'کالا های سفارش'
