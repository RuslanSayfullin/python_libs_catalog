# Generated by Django 4.0.2 on 2022-04-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directoryversion',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Версия'),
        ),
        migrations.AlterField(
            model_name='directoryversion',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
    ]
