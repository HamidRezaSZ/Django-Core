# Generated by Django 4.1.3 on 2023-02-01 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceOfMultipleChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('icon', models.FileField(blank=True, null=True, upload_to='', verbose_name='آیکون')),
                ('choice', models.CharField(max_length=200, verbose_name='مقدار')),
            ],
            options={
                'verbose_name': 'مقدار سوال چند گزینه ای',
                'verbose_name_plural': 'مقدار های سوال چند گزینه ای',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('question', models.TextField(verbose_name='سوال')),
                ('type', models.CharField(choices=[('MultipleChoice', 'چند گزینه ای'), ('Drop Down', 'کشویی'), ('File', 'فایل'), ('Descriptive', 'تشریحی')], default='Descriptive', max_length=20, verbose_name='نوع سوال')),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'سوال ها',
            },
        ),
        migrations.CreateModel(
            name='MultipleChoiceAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.choiceofmultiplechoicequestion', verbose_name='پاسخ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.question', verbose_name='سوال مربوطه')),
            ],
            options={
                'verbose_name': 'جواب چند گزینه ای',
                'verbose_name_plural': 'جواب های چند گزینه ای',
            },
        ),
        migrations.CreateModel(
            name='FileAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.FileField(upload_to='', verbose_name='فایل پاسخ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.question', verbose_name='سوال مربوطه')),
            ],
            options={
                'verbose_name': 'فایل جواب',
                'verbose_name_plural': 'فایل های جواب',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='زمان بروز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('questions', models.ManyToManyField(to='exam.question', verbose_name='سوالات')),
            ],
            options={
                'verbose_name': 'آزمون',
                'verbose_name_plural': 'آزمون ها',
            },
        ),
        migrations.CreateModel(
            name='DescriptiveAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='پاسخ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.question', verbose_name='سوال مربوطه')),
            ],
            options={
                'verbose_name': 'جواب تشریحی',
                'verbose_name_plural': 'جواب های تشریحی',
            },
        ),
        migrations.AddField(
            model_name='choiceofmultiplechoicequestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.question', verbose_name='سوال مربوطه'),
        ),
    ]
