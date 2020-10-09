# Generated by Django 3.1.1 on 2020-10-09 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20201001_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.IntegerField()),
                ('customerFName', models.CharField(max_length=100)),
                ('customerLName', models.CharField(max_length=100)),
                ('employeeEmail', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productID', models.IntegerField()),
                ('price', models.FloatField(max_length=11)),
                ('qty', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
            options={
                'db_table': 'OrderedProducts',
            },
        ),
    ]
