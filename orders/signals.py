from cart.models import Cart
from .models import OrderProductQuantity
from django.dispatch import receiver
from django.db.models.signals import post_save
from payments.models import Payment


@receiver(post_save, sender=Payment)
def order_payment_signal(sender, instance, update_fields, **kwargs):
    '''
        After order paid successflly
    '''

    created = False

    if 'created' in kwargs:
        if kwargs['created']:
            created = True

    if created or not (update_fields and 'status' in update_fields and instance.status == 'موفق'):
        return

    order_obj = instance.order_set.first()
    for item in instance.order_set.first().related_order_product_quantity.all():
        item.related_product_quantity.quantity -= item.quantity
        item.related_product_quantity.save()

    order_obj.status = 'پرداخت شده'
    order_obj.save()


@receiver(post_save, sender=OrderProductQuantity)
def add_to_cart_signal(sender, instance, *args, **kwargs):
    """
        Update Cart after OrderProductQuantity created
    """

    created = False

    if 'created' in kwargs:
        if kwargs['created']:
            created = True

    if not created:
        return

    cart_obj = Cart.objects.get(related_user=instance.related_user)
    cart_obj.related_order_product_quantity.add(instance)
    cart_obj.save()
