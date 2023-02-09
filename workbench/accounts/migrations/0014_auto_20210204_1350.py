# Generated by Django 3.2a1 on 2021-02-04 12:50

from django.conf import settings
from django.db import migrations


namespaces = {
    "feinheit": {
        "jg@feinheit.ch": {
            "BOOKKEEPING",
            "WORKING_TIME_CORRECTION",
        },
        "mk@feinheit.ch": {
            "BOOKKEEPING",
            "WORKING_TIME_CORRECTION",
        },
        "info@galerie-rosenberg.ch": {
            "LATE_LOGGING",
        },
    },
    "bf": {
        "mk@feinheit.ch": {
            "BOOKKEEPING",
            "CONTROLLING",
            "LABOR_COSTS",
            "WORKING_TIME_CORRECTION",
        },
        "moritz@blindflugstudios.com": {
            "BOOKKEEPING",
            "CONTROLLING",
            "LABOR_COSTS",
            "WORKING_TIME_CORRECTION",
        },
        "jeremy@blindflugstudios.com": {
            "BOOKKEEPING",
            "CONTROLLING",
            "LABOR_COSTS",
            "WORKING_TIME_CORRECTION",
        },
        "frederic@blindflugstudios.com": {
            "BOOKKEEPING",
            "CONTROLLING",
            "LABOR_COSTS",
            "WORKING_TIME_CORRECTION",
        },
    },
    "dbpag": {},
    "test": {},
}


def forwards(apps, schema_editor):
    namespace = namespaces[settings.NAMESPACE]
    for user in apps.get_model("accounts", "user").objects.filter(email__in=namespace):
        user._features = sorted(namespace[user.email])
        user.save()


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0013_user__features"),
    ]

    operations = [
        migrations.RunPython(forwards, lambda *a: None),
    ]
