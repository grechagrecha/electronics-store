from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q, QuerySet

from .models import Item, ItemCategory, Cart, OrderedItem, ItemAttribute, ItemAttributeValue
from .filters import ItemFilter
from .forms import ContactForm


class ShopView(ListView):
    model = Item
    queryset = model.objects.all()
    template_name = 'core/shop.html'
    context_object_name = 'items'
    paginate_by = 6

    filterset = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ItemFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filterset.form
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


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'


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


def add_to_favourites(request, *args, **kwargs):
    http_referer_url = request.META['HTTP_REFERER']
    return redirect(http_referer_url)


def add_to_cart(request, slug):
    if not request.user.is_authenticated:
        return redirect('account_login')

    http_referer_url = request.META['HTTP_REFERER']

    item = get_object_or_404(Item, slug=slug)
    ordered_item, _ = OrderedItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    cart_qs = Cart.objects.filter(user=request.user, ordered=False)

    if cart_qs.exists():
        cart = cart_qs[0]

        if cart.items.filter(item__slug=item.slug).exists():
            item.units_in_stock -= 1
            item.save()

            ordered_item.quantity += 1
            ordered_item.save()
        else:
            cart.items.add(ordered_item)
    else:
        ordered_date = timezone.now()
        cart = Cart.objects.create(user=request.user, ordered_date=ordered_date)
        cart.items.add(ordered_item)

        item.units_in_stock -= 1

    return redirect(http_referer_url)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    ordered_item, created = OrderedItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    cart_qs = Cart.objects.filter(user=request.user, ordered=False)

    if cart_qs.exists():
        cart = cart_qs[0]
        if cart.items.filter(item__slug=item.slug).exists():
            if ordered_item.quantity >= 2:
                ordered_item.quantity -= 1
                ordered_item.save()
            else:
                cart.items.remove(ordered_item)

            item.units_in_stock += 1

    return redirect('core:cart')


def order(request):
    order_status = True
    return render(request, 'core/order.html', context={
        'order_status': order_status
    })
