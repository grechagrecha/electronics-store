from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render

from .models import Item, ItemCategory, ShoppingCart


class StoreView(ListView):
    model = Item
    template_name = 'core/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_categories'] = ItemCategory.objects.all()
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'core/product.html'
    context_object_name = 'item'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        return render(request, self.template_name, context)


class HomeView(ListView):
    model = Item
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_categories'] = ItemCategory.objects.all()
        return context


class AboutView(TemplateView):
    model = None
    template_name = 'core/about.html'


class ContactView(TemplateView):
    model = None
    template_name = 'core/contact.html'


class CartView(TemplateView):
    model = ShoppingCart
    template_name = 'core/cart.html'


class ProfileView(TemplateView):
    model = ShoppingCart
    template_name = 'core/profile.html'
