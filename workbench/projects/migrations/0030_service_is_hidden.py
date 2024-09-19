# Generated by Django 5.1 on 2024-08-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0029_alter_internaltype_ordering"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="is_hidden",
            field=models.BooleanField(
                default=False,
                help_text="Hide services in the search",
                verbose_name="is hidden",
            ),
        ),
    ]
