from django.views.generic import ListView, DetailView, TemplateView

from .models import Item


class StoreView(ListView):
    model = Item
    template_name = 'core/shop.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/product.html'
    context_object_name = 'item'


class HomeView(ListView):
    model = Item
    template_name = 'core/home.html'


class AboutView(TemplateView):
    model = None
    template_name = 'core/about.html'


class ContactView(TemplateView):
    model = None
    template_name = 'core/contact.html'
