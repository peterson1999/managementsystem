# Generated by Django 3.1.1 on 2020-09-23 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20200923_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='regdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]