from collections import defaultdict
from itertools import chain

from django.utils.translation import gettext as _

from xlsxdocument import XLSXDocument

from workbench.contacts.models import PostalAddress
from workbench.tools.formats import H1


class WorkbenchXLSXDocument(XLSXDocument):
    def logged_hours(self, queryset):
        queryset = queryset.select_related(
            "created_by",
            "rendered_by",
            "service__project__owned_by",
            "invoice_service__invoice__owned_by",
            "invoice_service__invoice__project",
        )

        self.table_from_queryset(
            queryset,
            additional=[
                (_("hourly rate"), lambda hours: hours.service.effort_rate),
                (_("project"), lambda hours: hours.service.project),
                (
                    _("invoice"),
                    lambda hours: hours.invoice_service.invoice
                    if hours.invoice_service
                    else None,
                ),
            ],
        )

        by_service_and_user = defaultdict(lambda: defaultdict(lambda: H1))

        for h in queryset:
            by_service_and_user[h.service][h.rendered_by] += h.hours

        self.add_sheet(_("by service and user"))
        users = sorted(
            set(
                chain.from_iterable(
                    users.keys() for users in by_service_and_user.values()
                )
            )
        )

        self.table(
            [_("project"), _("service"), _("hourly rate"), _("total")]
            + [user.get_short_name() for user in users],
            [
                [
                    service.project,
                    service,
                    service.effort_rate,
                    sum(by_users.values(), H1),
                ]
                + [by_users.get(user) for user in users]
                for service, by_users in sorted(
                    by_service_and_user.items(),
                    key=lambda row: (row[0].project_id, row[0].position),
                )
            ],
        )

    def logged_costs(self, queryset):
        self.table_from_queryset(
            queryset.select_related(
                "created_by",
                "rendered_by",
                "service__project__owned_by",
                "invoice_service__invoice__owned_by",
                "invoice_service__invoice__project",
            ),
            additional=[
                ("service", lambda cost: cost.service),
                ("project", lambda cost: cost.service.project),
                (
                    "invoice",
                    lambda cost: cost.invoice_service.invoice
                    if cost.invoice_service
                    else None,
                ),
            ],
        )

    def people(self, queryset):
        addresses = {
            address.person_id: address
            for address in PostalAddress.objects.filter(person__in=queryset).reverse()
        }

        def getter(field):
            def attribute(person):
                return getattr(addresses.get(person.id), field, "")

            return attribute

        self.table_from_queryset(
            queryset.select_related("organization", "primary_contact"),
            additional=[
                (field, getter(field))
                for field in [
                    "street",
                    "house_number",
                    "address_suffix",
                    "postal_code",
                    "city",
                    "country",
                    "postal_address_override",
                ]
            ],
        )

    def project_budget_statistics(self, statistics):
        self.add_sheet(_("projects"))
        self.table(
            [
                _("project"),
                _("responsible"),
                _("offered"),
                _("logbook"),
                _("undefined rate"),
                _("third party costs"),
                _("invoiced"),
                _("not archived"),
                _("total hours"),
                _("delta"),
            ],
            [
                (
                    project["project"],
                    project["project"].owned_by.get_short_name(),
                    project["offered"],
                    project["logbook"],
                    project["effort_hours_with_rate_undefined"],
                    project["third_party_costs"],
                    project["invoiced"],
                    project["not_archived"],
                    project["hours"],
                    project["delta"],
                )
                for project in statistics["statistics"]
            ],
        )
