# Generated by Django 4.1.7 on 2023-03-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0007_remove_service_info_simage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service_info",
            name="sdesc",
            field=models.CharField(max_length=150),
        ),
    ]
