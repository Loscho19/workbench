# Generated by Django 3.2.14 on 2022-09-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0023_auto_20220909_2132"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internaltype",
            name="percentage",
            field=models.DecimalField(
                decimal_places=2, max_digits=5, verbose_name="percentage"
            ),
        ),
    ]
