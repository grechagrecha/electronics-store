from django.urls import path

from . import views


app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shop', views.ShopView.as_view(), name='shop'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('cart', views.CartView.as_view(), name='cart'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('add-to-cart/<slug>', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', views.remove_from_cart, name='remove-from-cart'),
    path('order', views.order, name='order'),

]
