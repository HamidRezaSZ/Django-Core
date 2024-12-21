from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models.base_model import BaseModel

class FAQ(BaseModel):
    question = models.CharField(verbose_name=_('question'), max_length=500)
    answer = models.TextField(verbose_name=_('answer'))

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self) -> str:
        return self.question
