from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, Profile
from cart.models import Cart


@receiver(post_save, sender=User)
def application_signal(sender, instance, *args, **kwargs):
    """
        Create profile object after user created
    """

    created = False

    if 'created' in kwargs:
        if kwargs['created']:
            created = True

    if not created:
        return

    Profile.objects.create(user=instance)
    Cart.objects.create(user=instance)
