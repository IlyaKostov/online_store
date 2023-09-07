# Generated by Django 4.2.4 on 2023-09-07 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_contact_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='last_change_date',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
    ]