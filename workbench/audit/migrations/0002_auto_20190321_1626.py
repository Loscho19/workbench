# Generated by Django 2.1.7 on 2019-03-21 15:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("audit", "0001_initial"),
        ("credit_control", "0003_auto_20190321_1447"),
        ("logbook", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            "UPDATE audit_logged_actions SET row_data=delete(row_data, 'fts_document');"
            "UPDATE audit_logged_actions SET changed_fields=delete(changed_fields, 'fts_document');"
        ),
        migrations.RunSQL(
            "SELECT audit_audit_table('contacts_organization', ARRAY['fts_document']);"
            "SELECT audit_audit_table('contacts_person', ARRAY['fts_document']);"
            "SELECT audit_audit_table('credit_control_creditentry', ARRAY['fts_document']);"
            "SELECT audit_audit_table('invoices_invoice', ARRAY['fts_document']);"
            "SELECT audit_audit_table('invoices_recurringinvoice', ARRAY['fts_document']);"
            "SELECT audit_audit_table('logbook_loggedhours', ARRAY['fts_document']);"
            "SELECT audit_audit_table('logbook_loggedcost', ARRAY['fts_document']);"
            "SELECT audit_audit_table('offers_offer', ARRAY['fts_document']);"
            "SELECT audit_audit_table('projects_project', ARRAY['fts_document']);"
            "UPDATE contacts_organization SET id=id;"
            "UPDATE contacts_person SET id=id;"
            "UPDATE credit_control_creditentry SET id=id;"
            "UPDATE invoices_invoice SET id=id;"
            "UPDATE invoices_recurringinvoice SET id=id;"
            "UPDATE logbook_loggedhours SET id=id;"
            "UPDATE logbook_loggedcost SET id=id;"
            "UPDATE offers_offer SET id=id;"
            "UPDATE projects_project SET id=id;"
        ),
    ]
