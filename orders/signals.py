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
    for item in order_obj.orderitem_set.all():
        item.product_quantity.quantity -= item.quantity
        item.product_quantity.save()

    order_obj.status = 'پرداخت شده'
    order_obj.save()
