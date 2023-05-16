from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserExam
from .tasks import create_result


@receiver(post_save, sender=UserExam)
def after_exam_finished_signal(sender, instance, update_fields, **kwargs):
    created = False

    if 'created' in kwargs:
        if kwargs['created']:
            created = True

    if not created:
        return

    create_result.apply_async(
        (instance.user.pk, instance.exam.pk), countdown=instance.exam.duration.seconds)
