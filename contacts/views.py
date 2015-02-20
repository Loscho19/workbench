from collections import OrderedDict

from django.shortcuts import redirect

from contacts.forms import (
    OrganizationSearchForm, PhoneNumberFormset, EmailAddressFormset,
    PostalAddressFormset)
from contacts.models import (
    Organization, Person, PhoneNumber, EmailAddress, PostalAddress)
from tools.views import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)


class OrganizationViewMixin(object):
    model = Organization
    allow_delete_if_only = {Organization}


class PersonViewMixin(object):
    model = Person
    allow_delete_if_only = {
        Person, PhoneNumber, EmailAddress, PostalAddress}


class OrganizationListView(OrganizationViewMixin, ListView):
    def get_queryset(self):
        queryset = super().get_queryset()

        self.search_form = OrganizationSearchForm(self.request.GET)
        if self.search_form.is_valid():
            data = self.search_form.cleaned_data
            if data.get('g'):
                queryset = queryset.filter(groups=data.get('g'))

        return queryset
    pass


class OrganizationDetailView(OrganizationViewMixin, DetailView):
    pass


class OrganizationCreateView(OrganizationViewMixin, CreateView):
    def get_form(self, data=None, files=None, **kwargs):
        kwargs.setdefault('initial', {}).update({
            'primary_contact': self.request.user.pk,
        })
        form_class = self.get_form_class()
        return form_class(data, files, **kwargs)


class OrganizationUpdateView(OrganizationViewMixin, UpdateView):
    pass


class OrganizationDeleteView(OrganizationViewMixin, DeleteView):
    pass


class PersonListView(PersonViewMixin, ListView):
    def get_queryset(self):
        return super().get_queryset().select_related('organization')


class PersonDetailView(PersonViewMixin, DetailView):
    pass


class PersonCreateView(PersonViewMixin, CreateView):
    def get_form(self, data=None, files=None, **kwargs):
        kwargs.setdefault('initial', {}).update({
            'primary_contact': self.request.user.pk,
        })
        form_class = self.get_form_class()
        return form_class(data, files, **kwargs)


class PersonUpdateView(PersonViewMixin, UpdateView):
    def get_form(self, data=None, files=None, **kwargs):
        form_class = self.get_form_class()

        kw = {'data': data, 'files': files, 'instance': self.object}
        self.formsets = OrderedDict((
            ('phonenumbers', PhoneNumberFormset(**kw)),
            ('emailaddresses', EmailAddressFormset(**kw)),
            ('postaladdresses', PostalAddressFormset(**kw)),
        ))

        return form_class(data, files, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.allow_update():
            return redirect(self.object)

        form = self.get_form(
            data=request.POST, files=request.FILES, instance=self.object)
        if form.is_valid() and all(
                f.is_valid() for f in self.formsets.values()):
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        for formset in self.formsets.values():
            formset.save()
        return response


class PersonDeleteView(PersonViewMixin, DeleteView):
    pass
