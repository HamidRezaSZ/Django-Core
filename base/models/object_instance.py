from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class ObjectInstance(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    quantity = models.PositiveIntegerField()

    def clone_object(self, obj, attrs={}):
        clone = obj._meta.model.objects.get(pk=obj.pk)
        clone.pk = None

        for key, value in attrs.items():
            setattr(clone, key, value)

        clone.save()

        fields = clone._meta.get_fields()
        for field in fields:
            if not field.auto_created and field.many_to_many:
                for row in getattr(obj, field.name).all():
                    getattr(clone, field.name).add(row)

            if field.auto_created and field.is_relation:
                if field.many_to_many:
                    pass
                else:
                    attrs = {field.remote_field.name: clone}
                    children = field.related_model.objects.filter(
                        **{field.remote_field.name: obj}
                    )
                    for child in children:
                        try:
                            self.clone_object(child, attrs)
                        except Exception:
                            pass

        return clone

    def clean(self) -> None:
        try:
            self.content_type.get_object_for_this_type(id=self.object_id)
        except ObjectDoesNotExist:
            raise ValidationError(_("Content type with this object id not exist!"))

        return super().clean()

    def save(self, *args, **kwargs) -> None:
        obj = self.content_type.get_object_for_this_type(id=self.object_id)

        for _ in range(self.quantity):
            self.clone_object(obj)
