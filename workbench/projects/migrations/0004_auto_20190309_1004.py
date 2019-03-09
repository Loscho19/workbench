# Generated by Django 2.1.7 on 2019-03-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("projects", "0003_auto_20190306_2029")]

    operations = [
        migrations.RemoveField(model_name="project", name="invoicing"),
        migrations.RemoveField(model_name="project", name="maintenance"),
        migrations.RemoveField(model_name="project", name="status"),
        migrations.AddField(
            model_name="project",
            name="closed_on",
            field=models.DateField(blank=True, null=True, verbose_name="closed on"),
        ),
        migrations.AddField(
            model_name="project",
            name="type",
            field=models.CharField(
                choices=[
                    ("acquisition", "Acquisition"),
                    ("maintenance", "Maintenance"),
                    ("order", "Order"),
                    ("internal", "Internal"),
                ],
                default="order",
                max_length=20,
                verbose_name="type",
            ),
            preserve_default=False,
        ),
        migrations.AlterModelOptions(
            name="service",
            options={
                "ordering": ["position", "created_at"],
                "verbose_name": "service",
                "verbose_name_plural": "services",
            },
        ),
    ]
