from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("contact/", views.contact, name="Contact"),
    path("tracker/", views.tracker, name="Tracker"),
    path("search/", views.search, name="Search"),
    path("products/<int:id>", views.products, name="Products"),
    path("checkout/", views.checkout, name="Checkout"),
]