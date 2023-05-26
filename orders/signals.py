from django.db.models.signals import post_save
from django.dispatch import receiver

from payments.models import Payment

from .models import OrderStatus


@receiver(post_save, sender=Payment)
def order_payment_signal(sender, instance, update_fields, **kwargs):
    '''
        After order paid successflly
    '''

    created = False

    if 'created' in kwargs:
        if kwargs['created']:
            created = True

    if created or not (update_fields and 'status' in update_fields and instance.status.title == 'Successful'):
        return

    order_obj = instance.order_set.first()
    for item in order_obj.orderitem_set.all():
        item.product_quantity.quantity -= item.quantity
        item.product_quantity.save()

    status, created = OrderStatus.objects.get_or_create(status='Paid')
    order_obj.status = status
    order_obj.save()
