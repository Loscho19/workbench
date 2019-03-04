# Generated by Django 2.1.7 on 2019-03-04 12:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("projects", "0021_auto_20190304_1204")]

    operations = [
        migrations.AlterField(
            model_name="effort",
            name="billing_per_hour",
            field=models.DecimalField(
                decimal_places=2,
                default=None,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="billing per hour",
            ),
        )
    ]
