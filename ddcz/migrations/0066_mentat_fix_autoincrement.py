# Generated by Django 2.0.13 on 2021-04-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ddcz", "0065_mentat_drop_auto"),
    ]

    operations = [
        # Following migration doesn't work because Django generates multiple commands
        # that do not satisfy data constraints while running
        # migrations.AlterField(
        #     model_name="mentatnewbie",
        #     name="django_id",
        #     field=models.AutoField(default=1, primary_key=True, serialize=False),
        #     preserve_default=False,
        # ),
        migrations.RunSQL(
            "ALTER TABLE mentat_newbie MODIFY django_id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY;"
        ),
        migrations.RunSQL(
            """
                SET @m = (SELECT IFNULL(MAX(django_id) + 1, 1) FROM mentat_newbie);
                SET @s = CONCAT('ALTER TABLE mentat_newbie AUTO_INCREMENT=', @m);
                PREPARE stmt1 FROM @s;
                EXECUTE stmt1;
                DEALLOCATE PREPARE stmt1;
            """
        ),
    ]
