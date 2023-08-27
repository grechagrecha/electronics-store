from django.urls import path

from .views import HomeView, StoreView, ItemDetailView, AboutView, ContactView, CartView, ProfileView, add_to_cart


app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', StoreView.as_view(), name='shop'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('cart', CartView.as_view(), name='cart'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart')
]
