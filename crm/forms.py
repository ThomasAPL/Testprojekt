from django import forms
from .models import Address, Contact, AddressType




class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "type", "name", "address_line1", "address_line2",
            "postal_code", "city", "state", "country",
            "email", "phone", "vat_id", "notes",
            ]




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "address", "first_name", "last_name", "position",
            "email", "phone", "mobile", "is_primary",
            ]