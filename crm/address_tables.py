import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from .models import Address

class AddressTable(tables.Table):
    name = tables.LinkColumn('crm:address-detail', args=[tables.A('pk')])
    type = tables.Column(accessor='get_type_display', verbose_name='Typ')
    location = tables.Column(empty_values=(), verbose_name='Ort')
    email = tables.EmailColumn()
    actions = tables.Column(empty_values=(), verbose_name='')
    
    class Meta:
        model = Address
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "type", "location", "country", "phone", "email", "actions")
        attrs = {"class": "table table-striped"}
        
    def render_location(self, record):
        return f"{record.postal_code} {record.city}" if record.postal_code and record.city else ""
        
    def render_actions(self, record):
        edit_url = reverse('crm:address-update', args=[record.pk])
        return format_html('<a href="{}">Bearbeiten</a>', edit_url)