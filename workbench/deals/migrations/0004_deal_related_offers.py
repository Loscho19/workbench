# Generated by Django 3.0.4 on 2020-03-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("offers", "0008_auto_20190916_1110"),
        ("deals", "0003_valuetype_weekly_target"),
    ]

    operations = [
        migrations.AddField(
            model_name="deal",
            name="related_offers",
            field=models.ManyToManyField(
                blank=True,
                related_name="deals",
                to="offers.Offer",
                verbose_name="related offers",
            ),
        ),
    ]
