# Generated by Django 3.1b1 on 2020-06-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planning", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plannedwork",
            name="title",
            field=models.CharField(default="", max_length=200, verbose_name="title"),
            preserve_default=False,
        ),
    ]
