from django.db import models
from accounts.models import User


class Cart(models.Model):
    related_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')
    related_order_product_quantity = models.ManyToManyField(
        to='orders.OrderProductQuantity', null=True, verbose_name='کالای مربوطه', blank=True)

    def __str__(self):
        product_count = self.related_order_product_quantity.count()
        return '{} کالا توسط {}'.format(product_count, self.related_user.username)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'
