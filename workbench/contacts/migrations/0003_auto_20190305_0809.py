# Generated by Django 2.1.7 on 2019-03-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("contacts", "0002_auto_20190304_2247")]

    operations = [
        migrations.AddField(
            model_name="person",
            name="salutation",
            field=models.CharField(
                blank=True,
                help_text="Dear John/Dear Ms Smith",
                max_length=100,
                verbose_name="complete salutation",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="address",
            field=models.CharField(
                blank=True, help_text="Mr./Ms.", max_length=100, verbose_name="address"
            ),
        ),
    ]
