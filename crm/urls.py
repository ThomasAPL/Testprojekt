from django.urls import path
from . import views


app_name = "crm"


urlpatterns = [
    path("", views.AddressListView.as_view(), name="address-list"),
    #path("address/<int:pk>/", views.AddressDetailView.as_view(), name="address-detail"),
    path('addresses/', AddressListView.as_view(), name='address-list'),
    path("address/new/", views.AddressCreateView.as_view(), name="address-create"),
    path("address/<int:pk>/edit/", views.AddressUpdateView.as_view(), name="address-update"),
    path("address/<int:pk>/delete/", views.AddressDeleteView.as_view(), name="address-delete"),
    path("contact/new/", views.ContactCreateView.as_view(), name="contact-create"),
    path("contact/<int:pk>/edit/", views.ContactUpdateView.as_view(), name="contact-update"),
    path("contact/<int:pk>/delete/", views.ContactDeleteView.as_view(), name="contact-delete"),

    ]
