# Generated by Django 2.2.5 on 2019-09-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("invoices", "0014_auto_20190814_1609")]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="position",
            field=models.IntegerField(default=0, verbose_name="position"),
        )
    ]
