# Generated by Django 4.2.7 on 2024-02-17 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_chatmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
