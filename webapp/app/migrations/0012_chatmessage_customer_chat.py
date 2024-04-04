# Generated by Django 4.2.7 on 2024-02-16 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_adminmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='customer_chat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.customerchat'),
            preserve_default=False,
        ),
    ]
