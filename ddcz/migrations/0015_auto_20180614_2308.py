# Generated by Django 2.0.2 on 2018-06-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ddcz", "0014_auto_20180614_0032"),
    ]

    operations = [
        migrations.RenameModel("CommonArticles", "CommonArticle"),
        migrations.AlterField(
            model_name="creativepage",
            name="name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="creativepagesection",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
