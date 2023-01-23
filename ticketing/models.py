from django.db import models
from base.models import BaseModel
from accounts.models import User


class Ticket(models.Model):
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')
    is_archive = models.BooleanField(default=False, verbose_name='آرشیو شده')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        TicketMessage.objects.get_or_create(ticket=self)

    def __str__(self):
        return f'@{self.client}: {self.subject}'

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت'


class Department(BaseModel):
    name = models.CharField(max_length=200, verbose_name='نام')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        TicketDepartment.objects.get_or_create(department=self)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'دپارتمان'
        verbose_name_plural = 'دپارتمان'


class TicketDepartment(BaseModel):
    ticket = models.ManyToManyField(to=Ticket, verbose_name='تیکت')
    department = models.OneToOneField(to=Department, on_delete=models.CASCADE, verbose_name='دپارتمان')

    def __str__(self):
        return f'{self.department.name}'

    class Meta:
        verbose_name = 'دپارتمان تیکت'
        verbose_name_plural = 'دپارتمان های تیکت'


class Priority(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        TicketPriority.objects.get_or_create(priority=self)

    class Meta:
        verbose_name = 'اولویت'
        verbose_name_plural = 'اولویت ها'


class TicketPriority(BaseModel):
    ticket = models.ManyToManyField(to=Ticket, verbose_name='تیکت')
    priority = models.OneToOneField(to=Priority, verbose_name='اولویت', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.priority.title}'

    class Meta:
        verbose_name = 'اولویت تیکت'
        verbose_name_plural = 'اولویت های تیکت'


class Status(BaseModel):
    title = models.CharField(max_length=200, verbose_name='تایتل')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        TicketStatus.objects.get_or_create(status=self)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'وضعیت'
        verbose_name_plural = 'وضعیت ها'


class TicketStatus(BaseModel):
    ticket = models.ManyToManyField(to=Ticket, verbose_name='تیکت')
    status = models.OneToOneField(to=Status, verbose_name='وضعیت', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status.title}'

    class Meta:
        verbose_name = 'وضعیت تیکت'
        verbose_name_plural = 'وضعیت های تیکت'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    content = models.TextField(verbose_name='پیام')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        MessageFile.objects.get_or_create(message=self)

    def __str__(self):
        return f'@{self.user} {self.content}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class TicketMessage(BaseModel):
    ticket = models.OneToOneField(to=Ticket, verbose_name='تیکت', on_delete=models.CASCADE)
    message = models.ManyToManyField(to=Message, verbose_name='پیام')

    def __str__(self):
        return f'{self.ticket.subject}'

    class Meta:
        verbose_name = 'پیام تیکت'
        verbose_name_plural = 'پیام های تیکت'


class File(models.Model):
    file = models.FileField(verbose_name='فایل')

    def __str__(self):
        return f'{self.file}'

    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل ها'


class MessageFile(models.Model):
    message = models.OneToOneField(to=Message, verbose_name='پیام', on_delete=models.CASCADE)
    file = models.ManyToManyField(to=File, verbose_name='فایل')

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name = 'فایل پیام'
        verbose_name_plural = 'فایل های پیام'
