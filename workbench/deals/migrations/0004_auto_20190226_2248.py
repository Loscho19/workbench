# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 21:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("deals", "0003_auto_20160924_2201")]

    operations = [
        migrations.AlterField(
            model_name="deal",
            name="estimated_value",
            field=models.DecimalField(
                decimal_places=2,
                default=None,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="estimated value",
            ),
        )
    ]
