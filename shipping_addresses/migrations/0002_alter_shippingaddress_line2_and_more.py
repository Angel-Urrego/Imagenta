# Generated by Django 4.0.2 on 2023-03-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='line2',
            field=models.IntegerField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='postal_code',
            field=models.IntegerField(max_length=10),
        ),
    ]
