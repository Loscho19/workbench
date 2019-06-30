# Generated by Django 2.2.2 on 2019-06-30 20:20

from django.db import migrations


def forwards(apps, schema_editor):
    Model = apps.get_model("invoices.Invoice")
    for instance in Model.objects.select_related("customer", "contact"):
        instance._fts = " ".join(
            str(part)
            for part in [
                "%s-%04d-%04d"
                % (
                    instance.project.created_at.year,
                    instance.project._code,
                    instance._code,
                )
                if instance.project
                else "%05d" % instance._code,
                instance.customer.name,
                instance.contact.given_name if instance.contact else "",
                instance.contact.family_name if instance.contact else "",
                instance.project.title if instance.project else "",
            ]
        )
        instance.save()


class Migration(migrations.Migration):

    dependencies = [("invoices", "0012_invoice__fts")]

    operations = [migrations.RunPython(forwards)]
