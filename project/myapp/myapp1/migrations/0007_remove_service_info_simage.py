# Generated by Django 4.1.7 on 2023-03-03 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0006_alter_service_info_simage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service_info",
            name="simage",
        ),
    ]
