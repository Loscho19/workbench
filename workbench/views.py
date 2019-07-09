from django.apps import apps
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _

from workbench.audit.models import LoggedAction
from workbench.contacts.models import Organization, Person
from workbench.deals.models import Deal
from workbench.invoices.models import Invoice, RecurringInvoice
from workbench.offers.models import Offer
from workbench.projects.models import Project
from workbench.tools.history import changes


def search(request):
    results = []
    q = request.GET.get("q", "")
    if q:
        results = [
            {
                "verbose_name_plural": queryset.model._meta.verbose_name_plural,
                "url": reverse(
                    "%s_%s_list"
                    % (queryset.model._meta.app_label, queryset.model._meta.model_name)
                ),
                "results": queryset.search(q)[:101],
            }
            for queryset in (
                Project.objects.select_related("owned_by"),
                Organization.objects.all(),
                Person.objects.all(),
                Invoice.objects.select_related("project", "owned_by"),
                RecurringInvoice.objects.all(),
                Offer.objects.select_related("project", "owned_by"),
                Deal.objects.all(),
            )
        ]
    else:
        messages.error(request, _("Search query missing."))

    return render(request, "search.html", {"query": q, "results": results})


HISTORY = {
    "accounts.user": {"exclude": {"is_admin", "last_login", "password"}},
    "contacts.person": {"exclude": {"_fts"}},
    "invoices.invoice": {"exclude": {"_code", "_fts"}},
    "invoices.service": {"exclude": {"position"}},
    "offers.offer": {"exclude": {"_code"}},
    "projects.project": {"exclude": {"_code", "_fts"}},
    "projects.service": {"exclude": {"position"}},
}


def history(request, label, pk):
    model = apps.get_model(label)
    cfg = HISTORY.get(label, {})
    exclude = cfg.get("exclude", set())

    fields = [
        f.name
        for f in model._meta.get_fields()
        if hasattr(f, "attname") and not f.primary_key and f.name not in exclude
    ]

    try:
        instance = model._base_manager.get(pk=pk)
    except (model.DoesNotExist, TypeError, ValueError):
        instance = None

    return render(
        request,
        "history_modal.html",
        {
            "instance": instance,
            "changes": changes(
                model, fields, LoggedAction.objects.for_model_id(model, pk)
            ),
        },
    )
