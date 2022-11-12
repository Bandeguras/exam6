# Generated by Django 4.1.3 on 2022-11-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='completion_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
