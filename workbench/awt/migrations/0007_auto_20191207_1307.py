# Generated by Django 3.0 on 2019-12-07 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("awt", "0006_auto_20191207_1304"),
    ]

    operations = [
        migrations.AlterField(
            model_name="year",
            name="working_time_model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="awt.WorkingTimeModel",
                verbose_name="working time model",
            ),
        ),
        migrations.AlterField(
            model_name="year",
            name="year",
            field=models.IntegerField(verbose_name="year"),
        ),
        migrations.AlterUniqueTogether(
            name="year",
            unique_together={("working_time_model", "year")},
        ),
    ]
