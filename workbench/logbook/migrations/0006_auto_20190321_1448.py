# Generated by Django 2.1.7 on 2019-03-21 13:48

from django.db import migrations

from workbench.tools import search


class Migration(migrations.Migration):
    dependencies = [("logbook", "0005_auto_20190312_1254")]

    operations = [
        migrations.RunSQL(search.drop_old_fts("logbook_loggedcost")),
        migrations.RunSQL(search.drop_old_fts("logbook_loggedhours")),
        migrations.RunSQL(search.create_structure("logbook_loggedcost")),
        migrations.RunSQL(search.create_structure("logbook_loggedhours")),
        migrations.RunSQL(search.fts("logbook_loggedcost", ["description"])),
        migrations.RunSQL(search.fts("logbook_loggedhours", ["description"])),
    ]
