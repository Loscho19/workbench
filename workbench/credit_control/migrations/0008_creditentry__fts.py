# Generated by Django 3.0.2 on 2020-01-05 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("credit_control", "0007_auto_20200104_0938"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditentry",
            name="invoice",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="invoices.Invoice",
                verbose_name="invoice",
            ),
        ),
    ]
