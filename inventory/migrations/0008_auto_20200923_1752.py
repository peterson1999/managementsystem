# Generated by Django 3.1.1 on 2020-09-23 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20200923_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='regdate',
            field=models.DateField(default=datetime.datetime(2020, 9, 23, 17, 52, 47, 4345)),
        ),
    ]