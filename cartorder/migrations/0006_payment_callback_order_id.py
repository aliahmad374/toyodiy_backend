# Generated by Django 4.1.11 on 2023-11-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartorder', '0005_alter_payment_callback_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_callback',
            name='order_id',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
