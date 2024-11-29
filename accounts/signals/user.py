from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile, User
from cart.models import Cart


@receiver(post_save, sender=User)
def initial_acccount_signal(sender, instance, *args, **kwargs):
    """
    Create profile object after user created
    """

    created = False

    if "created" in kwargs:
        if kwargs["created"]:
            created = True

    if not created:
        return

    Profile.objects.create(user=instance)
    Cart.objects.create(user=instance)
