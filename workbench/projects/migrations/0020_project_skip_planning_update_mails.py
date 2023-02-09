# Generated by Django 3.2.4 on 2021-10-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0019_auto_20200523_0929"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="suppress_planning_update_mails",
            field=models.BooleanField(
                default=False,
                verbose_name="suppress planning update mails for this project for everyone",
            ),
        ),
    ]
