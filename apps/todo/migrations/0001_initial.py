# Generated by Django 4.2.3 on 2023-07-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Описание')),
                ('completed', models.BooleanField(default=False, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Такси',
                'verbose_name_plural': 'Таски',
            },
        ),
    ]
