# Generated by Django 2.1.7 on 2019-03-04 21:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("accounts", "0001_initial"), ("audit", "0001_initial")]

    operations = [migrations.RunSQL("SELECT audit_audit_table('accounts_user')")]
