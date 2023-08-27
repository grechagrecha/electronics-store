from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Item, ItemCategory, Cart, OrderedItem


class StoreView(ListView):
    model = Item
    template_name = 'core/shop.html'
    paginate_by = 6

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

        context['featured_products'] = Item.objects.filter().order_by('-id')[:6]
        context['featured_categories'] = ItemCategory.objects.filter().order_by('-id')[:3]

        return context


class AboutView(TemplateView):
    model = None
    template_name = 'core/about.html'


class ContactView(TemplateView):
    model = None
    template_name = 'core/contact.html'


class CartView(ListView):
    model = Cart
    template_name = 'core/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart_qs = context['cart_list'][0]

        context['user'] = cart_qs.user
        context['items'] = cart_qs.items.all()

        # :(
        # context['date'] = cart_qs.date

        return context


class ProfileView(TemplateView):
    model = Cart
    template_name = 'core/profile.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    ordered_item, created = OrderedItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Cart.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            ordered_item.quantity += 1
            ordered_item.save()
        else:
            order.items.add(ordered_item)
    else:
        ordered_date = timezone.now()
        order = Cart.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(ordered_item)
    return redirect('core:product', slug=slug)
