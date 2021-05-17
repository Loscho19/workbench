# Generated by Django 3.2.2 on 2021-05-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planning", "0012_auto_20210429_1448"),
    ]

    operations = [
        migrations.CreateModel(
            name="PublicHoliday",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="date")),
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "fraction",
                    models.DecimalField(
                        decimal_places=2,
                        default=1,
                        max_digits=5,
                        verbose_name="fraction of day which is free",
                    ),
                ),
            ],
            options={
                "verbose_name": "public holiday",
                "verbose_name_plural": "public holidays",
                "ordering": ["-date"],
            },
        ),
        migrations.RunSQL(
            "SELECT audit_audit_table('planning_publicholiday');",
            "",
        ),
    ]
