from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse



class AddressType(models.TextChoices):
    CUSTOMER = "customer", _("Kunde")
    SUPPLIER = "supplier", _("Lieferant")
    GENERAL = "general", _("Allgemein")




class Address(models.Model):
    type = models.CharField(max_length=20,choices=AddressType.choices,default=AddressType.CUSTOMER,verbose_name=_("Typ"),)
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    address_line1 = models.CharField(max_length=200, verbose_name=_("Straße und Nr."))
    address_line2 = models.CharField(max_length=200, blank=True, verbose_name=_("Adresszusatz"))
    postal_code = models.CharField(max_length=20, verbose_name=_("PLZ"))
    city = models.CharField(max_length=100, verbose_name=_("Ort"))
    state = models.CharField(max_length=100, blank=True, verbose_name=_("Bundesland"))
    country = models.CharField(max_length=100, default="Deutschland", verbose_name=_("Land"))
    email = models.EmailField(blank=True, verbose_name=_("E-Mail"))
    phone = models.CharField(max_length=50, blank=True, verbose_name=_("Telefon"))
    vat_id = models.CharField(max_length=32, blank=True, verbose_name=_("USt-IdNr."))
    notes = models.TextField(blank=True, verbose_name=_("Notizen"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Adresse")
        verbose_name_plural = _("Adressen")

    def get_absolute_url(self):
        return reverse("crm:address-detail", args=[str(self.pk)])

    def __str__(self):
        return self.name




class Contact(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="contacts", verbose_name=_("Adresse"))
    first_name = models.CharField(max_length=100, verbose_name=_("Vorname"))
    last_name = models.CharField(max_length=100, verbose_name=_("Nachname"))
    position = models.CharField(max_length=100, blank=True, verbose_name=_("Funktion"))
    email = models.EmailField(blank=True, verbose_name=_("E-Mail"))
    phone = models.CharField(max_length=50, blank=True, verbose_name=_("Telefon"))
    mobile = models.CharField(max_length=50, blank=True, verbose_name=_("Mobil"))
    is_primary = models.BooleanField(default=False, verbose_name=_("Hauptansprechpartner"))


class Meta:
    ordering = ["last_name", "first_name"]
    verbose_name = _("Ansprechpartner")
    verbose_name_plural = _("Ansprechpartner")
    constraints = [models.UniqueConstraint(fields=["address", "email"], name="uniq_contact_email_per_address")]


def __str__(self):
    return f"{self.first_name} {self.last_name}".strip()
