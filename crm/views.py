from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
    )


from .models import Address, Contact, AddressType
from .forms import AddressForm, ContactForm

class AddressListView(ListView):
    model = Address
    template_name = "crm/address_list.html"
    context_object_name = "addresses"
    paginate_by = 20  # Serverseitige Paginierung

    def get_queryset(self):
        qs = Address.objects.all()
        q = self.request.GET.get("q", "").strip()
        t = self.request.GET.get("type", "").strip()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(city__icontains=q) |
                Q(email__icontains=q) |
                Q(phone__icontains=q)
            )
        if t in dict(AddressType.choices):
            qs = qs.filter(type=t)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filter_q"] = self.request.GET.get("q", "")
        ctx["filter_type"] = self.request.GET.get("type", "")
        ctx["types"] = AddressType.choices
        return ctx


class AddressDetailView(DetailView):
    model = Address
    template_name = "crm/address_detail.html"
    context_object_name = "address"


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = "crm/address_form.html"


class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = "crm/address_form.html"


class AddressDeleteView(DeleteView):
    model = Address
    template_name = "crm/address_confirm_delete.html"
    success_url = reverse_lazy("crm:address-list")


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "crm/contact_form.html"

    def get_initial(self):
        initial = super().get_initial()
        address_id = self.request.GET.get("address")
        if address_id:
            initial["address"] = address_id
        return initial


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "crm/contact_form.html"


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = "crm/contact_confirm_delete.html"

    def get_success_url(self):
        # Nach dem Löschen zurück zur zugehörigen Adresse
        address = self.object.address
        return address.get_absolute_url() if hasattr(address, "get_absolute_url") else reverse_lazy("crm:address-list")