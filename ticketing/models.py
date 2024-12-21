from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from base.models.base_model import BaseModel


class TicketDepartment(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("name"))

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self) -> str:
        return f"{self.name}"


class TicketPriority(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))

    class Meta:
        verbose_name = _("Priority")
        verbose_name_plural = _("Priorities")

    def __str__(self) -> str:
        return self.title


class TicketStatus(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("title"))

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")

    def __str__(self) -> str:
        return self.title


class Ticket(models.Model):
    subject = models.CharField(max_length=200, verbose_name=_("subject"))
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("client"))
    department = models.ForeignKey(
        to=TicketDepartment, verbose_name=_("department"), on_delete=models.PROTECT
    )
    priority = models.ForeignKey(
        to=TicketPriority, on_delete=models.PROTECT, verbose_name=_("priority")
    )
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("created_date")
    )
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_("modified_date"))
    is_archive = models.BooleanField(default=False, verbose_name=_("is_archive"))
    status = models.ForeignKey(
        to=TicketStatus, verbose_name=_("status"), on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")

    def __str__(self) -> str:
        return f"@{self.client}: {self.subject}"


class TicketMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    ticket = models.ForeignKey(
        to=Ticket, verbose_name=_("ticket"), on_delete=models.CASCADE
    )
    content = models.TextField(verbose_name=_("content"))

    class Meta:
        verbose_name = _("Messages")
        verbose_name_plural = _("Messageses")

    def __str__(self) -> str:
        return f"@{self.user} {self.content}"


class MessageFile(models.Model):
    message = models.ForeignKey(
        to=TicketMessage, verbose_name=_("message"), on_delete=models.CASCADE
    )
    file = models.FileField(verbose_name=_("file"))

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")

    def __str__(self) -> str:
        return f"{self.file}"
