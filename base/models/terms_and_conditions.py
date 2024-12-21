from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel


class TermsAndConditions(BaseModel):
    text = RichTextUploadingField(verbose_name=_("text"))

    class Meta:
        verbose_name = _("Terms And Conditions")
        verbose_name_plural = _("Terms And Conditions")
