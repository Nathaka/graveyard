# Generated by Django 2.0.13 on 2020-10-10 16:09

import ddcz.models.magic
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ddcz", "0026_links"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Linky",
            new_name="Link",
        ),
    ]
