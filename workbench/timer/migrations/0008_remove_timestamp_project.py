# Generated by Django 3.1.2 on 2020-10-21 07:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("timer", "0007_auto_20200506_2130"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timestamp",
            name="project",
        ),
    ]
