# Generated by Django 4.1.7 on 2023-03-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0003_service_info_simage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service_info",
            name="simage",
            field=models.ImageField(default="", upload_to="myapp1/images"),
        ),
    ]
