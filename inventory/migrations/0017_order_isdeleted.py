# Generated by Django 3.1.1 on 2020-10-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_product_isdeleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
