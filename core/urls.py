from django.urls import path


from .views import HomeView, StoreView, ItemDetailView, AboutView, ContactView


app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', StoreView.as_view(), name='shop'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact')

]
