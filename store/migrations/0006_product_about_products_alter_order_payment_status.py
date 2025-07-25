# Generated by Django 5.2.2 on 2025-07-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_payment_error_order_ref_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about_products',
            field=models.TextField(blank=True, help_text='Brief introduction about the product', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('completed', 'Completed'), ('failed', 'Failed'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
    ]
