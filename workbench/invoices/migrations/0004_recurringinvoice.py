# Generated by Django 2.1.7 on 2019-03-06 20:04

import datetime
from decimal import Decimal

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contacts", "0003_auto_20190305_0809"),
        ("invoices", "0003_auto_20190304_2247"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecurringInvoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subtotal",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="subtotal",
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="discount",
                    ),
                ),
                (
                    "liable_to_vat",
                    models.BooleanField(
                        default=True,
                        help_text="For example invoices to foreign institutions are not liable to VAT.",
                        verbose_name="liable to VAT",
                    ),
                ),
                (
                    "tax_rate",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("7.7"),
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="tax rate",
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="total",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="created at"
                    ),
                ),
                ("postal_address", models.TextField(verbose_name="postal address")),
                (
                    "starts_on",
                    models.DateField(
                        default=datetime.date.today, verbose_name="starts on"
                    ),
                ),
                (
                    "ends_on",
                    models.DateField(
                        blank=True, null=True, verbose_name="cancel the auto-renewal on"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("yearly", "yearly"),
                            ("quarterly", "quarterly"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly"),
                        ],
                        max_length=20,
                        verbose_name="periodicity",
                    ),
                ),
                (
                    "next_period_starts_on",
                    models.DateField(
                        blank=True, null=True, verbose_name="next period starts on"
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contacts.Person",
                        verbose_name="contact",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="contacts.Organization",
                        verbose_name="customer",
                    ),
                ),
                (
                    "owned_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="contact person",
                    ),
                ),
            ],
            options={
                "verbose_name": "recurring invoice",
                "verbose_name_plural": "recurring invoices",
                "ordering": ["customer__name", "title"],
            },
        ),
        migrations.RunSQL("SELECT audit_audit_table('invoices_recurringinvoice');", ""),
    ]
