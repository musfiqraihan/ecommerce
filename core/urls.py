from django.urls import path
from .views import (
    HomeView,
    checkout_page,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product/details/<slug>', ItemDetailView.as_view(), name="product"),
    path('product/add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('product/remove-from-cart/<slug>', remove_from_cart, name="remove-from-cart"),
    path('checkout/', checkout_page, name="checkout"),
]