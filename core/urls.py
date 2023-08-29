from django.urls import path

from .views import HomeView, ShopView, ItemDetailView, AboutView, ContactView, CartView, ProfileView, add_to_cart, order


app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('cart', CartView.as_view(), name='cart'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('order', order, name='order')
]
