# Generated by Django 3.0.6 on 2020-05-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logbook", "0019_auto_20200511_1330"),
    ]

    operations = [
        migrations.AlterField(
            model_name="break",
            name="ends_at",
            field=models.DateTimeField(verbose_name="ends at"),
        ),
        migrations.AlterField(
            model_name="break",
            name="starts_at",
            field=models.DateTimeField(verbose_name="starts at"),
        ),
    ]
