# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 21:48
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("invoices", "0009_invoice__code")]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="discount",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="discount",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="down_payment_total",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="down payment total",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="subtotal",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="subtotal",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="tax_rate",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("7.7"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="tax rate",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="total",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0"),
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="total",
            ),
        ),
    ]
