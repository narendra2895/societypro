# Generated by Django 4.1.7 on 2023-03-03 20:03

import datetime
from django.db import migrations, models
import myapp1.models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0008_alter_service_info_sdesc"),
    ]

    operations = [
        migrations.CreateModel(
            name="blog_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "btitle",
                    models.CharField(
                        max_length=50, validators=[myapp1.models.check_space]
                    ),
                ),
                ("bcontent", models.TextField(validators=[myapp1.models.check_space])),
                ("bdate", models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
