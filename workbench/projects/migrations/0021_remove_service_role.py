# Generated by Django 3.2.14 on 2022-09-08 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0020_project_skip_planning_update_mails"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="role",
        ),
    ]
