# Generated by Django 3.2rc1 on 2021-04-06 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0005_servicetype_color"),
        ("planning", "0011_alter_plannedwork_created_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="plannedwork",
            name="service_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="services.servicetype",
                help_text="Colorize the work unit according to its service type.",
                verbose_name="service type",
            ),
        ),
    ]
