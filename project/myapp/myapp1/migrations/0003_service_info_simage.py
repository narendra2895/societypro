# Generated by Django 4.1.7 on 2023-03-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0002_service_info_alter_record_model_cemail_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="service_info",
            name="simage",
            field=models.ImageField(default="", upload_to="service/images"),
        ),
    ]
