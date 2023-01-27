from django.db import models
from base.models import BaseModel
from accounts.models import User


class TicketDepartment(BaseModel):
    name = models.CharField(max_length=200, verbose_name='نام')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'دپارتمان'
        verbose_name_plural = 'دپارتمان'


class TicketPriority(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اولویت'
        verbose_name_plural = 'اولویت ها'


class TicketStatus(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت ها'


class Ticket(models.Model):
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    department = models.ForeignKey(to=TicketDepartment, verbose_name='دپارتمان', on_delete=models.PROTECT)
    priority = models.ForeignKey(to=TicketPriority, on_delete=models.PROTECT, verbose_name='اولویت')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')
    is_archive = models.BooleanField(default=False, verbose_name='آرشیو شده')
    status = models.ForeignKey(to=TicketStatus, verbose_name='وضعیت', on_delete=models.PROTECT)

    def __str__(self):
        return f'@{self.client}: {self.subject}'

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت'


class TicketMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    ticket = models.OneToOneField(to=Ticket, verbose_name='تیکت', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='پیام')

    def __str__(self):
        return f'@{self.user} {self.content}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class MessageFile(models.Model):
    message = models.OneToOneField(to=TicketMessage, verbose_name='پیام', on_delete=models.CASCADE)
    file = models.FileField(verbose_name='فایل')

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل ها'
