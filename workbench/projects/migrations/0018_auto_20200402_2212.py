# Generated by Django 3.0.4 on 2020-04-02 20:12

from django.db import migrations

from workbench.tools import search


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0017_project_cost_center"),
    ]

    operations = [
        migrations.RunSQL(search.create_structure("projects_service")),
        migrations.RunSQL(search.fts("projects_service", ["title", "description"])),
        migrations.RunSQL(
            "SELECT audit_audit_table('projects_service', ARRAY['fts_document', 'position']);"
        ),
        migrations.RunSQL("UPDATE projects_service SET id=id"),
    ]
