# Generated by Django 5.0.6 on 2025-02-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_api', '0002_remove_review_booking_delete_payment_delete_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomimage',
            name='image',
            field=models.CharField(default='', max_length=100),
        ),
    ]
