# Generated by Django 3.1.1 on 2020-10-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_merge_20200923_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='static/images/'),
        ),
    ]
