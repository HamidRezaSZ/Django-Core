from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

from base.models.base_model import BaseModel


class AboutUs(BaseModel):
    text = RichTextUploadingField(verbose_name=_("text"))

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")
