# Generated by Django 4.2.7 on 2024-02-13 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_order_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]