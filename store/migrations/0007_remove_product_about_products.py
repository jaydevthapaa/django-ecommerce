# Generated by Django 5.2.2 on 2025-07-16 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_about_products_alter_order_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='about_products',
        ),
    ]
