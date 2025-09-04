import django_tables2 as tables
from .models import Address

class AddressTable(tables.Table):
    class Meta:
        model = Address
        template_name = "django_tables2/bootstrap.html"
        fields = ("id", "street", "city", "zip_code", "country")