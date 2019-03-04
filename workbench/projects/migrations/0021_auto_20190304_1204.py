# Generated by Django 2.1.7 on 2019-03-04 11:04

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("projects", "0020_cost_third_party_costs")]

    operations = [
        migrations.AddField(
            model_name="effort",
            name="billing_per_hour",
            field=models.DecimalField(
                decimal_places=2,
                default=None,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="billing per hour",
            ),
        ),
        migrations.AddField(
            model_name="effort",
            name="title",
            field=models.CharField(default="", max_length=200, verbose_name="title"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="effort",
            name="service_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="services.ServiceType",
                verbose_name="service type",
            ),
        ),
        migrations.RunSQL(
            """\
UPDATE projects_effort
SET billing_per_hour=st.billing_per_hour, title=st.title
FROM services_servicetype st
WHERE projects_effort.service_type_id=st.id
"""
        ),
    ]
