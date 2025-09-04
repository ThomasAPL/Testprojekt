from django.contrib import admin
from .models import Address, Contact


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "city", "country", "phone", "email")
    list_filter = ("type", "country")
    search_fields = ("name", "city", "email", "phone")
    inlines = [ContactInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "address", "email", "phone", "is_primary")
    list_filter = ("is_primary",)
    search_fields = ("last_name", "first_name", "email", "address__name")
