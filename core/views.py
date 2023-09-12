from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse

from .models import Item, ItemCategory, Cart, OrderedItem, ItemAttribute


class ShopView(ListView):
    model = Item
    template_name = 'core/shop.html'
    paginate_by = 6

    ITEM_CATEGORIES = [
        str(category.name_lowercase) for category in ItemCategory.objects.all()
    ]

    def _validate_sort_params(self, sort_params):
        validated_sort_params = dict()
        for key, value in sort_params.items():
            if value:
                if key == 'category':
                    if value in self.ITEM_CATEGORIES:
                        validated_sort_params[key] = value
        return validated_sort_params

    def get_sort_params(self):
        return {
            'category': self.request.GET.get('category')
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sort_params = self.get_sort_params()
        sort_params = self._validate_sort_params(sort_params)

        if sort_params:
            context['items'] = self.model.objects.filter(
                itemcategory__name_lowercase=sort_params.get('category')
            )
        else:
            context['items'] = self.model.objects.all()

        context['item_categories'] = ItemCategory.objects.all()
        context['item_attributes'] = ItemAttribute.objects.all()
        context['screen_resolution_attr'] = ItemAttribute.objects.filter(name='Screen resolution')
        context['refresh_rate_attr'] = ItemAttribute.objects.filter(name='Refresh rate')
        return context

    def get_queryset(self):
        qs_filter_category = self.request.GET.get('category', '')
        if not qs_filter_category or qs_filter_category == 'all':
            return self.model.objects.all().order_by('name')
        return self.model.objects.filter(itemcategory__name_lowercase=qs_filter_category).order_by('name')


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


def add_to_favourites(request, *args, **kwargs):
    http_referer_url = request.META['HTTP_REFERER']
    return redirect(http_referer_url)


def add_to_cart(request, slug):
    if not request.user.is_authenticated:
        return redirect('account_login')
    
    http_referer_url = request.META['HTTP_REFERER']

    item = get_object_or_404(Item, slug=slug)
    ordered_item, created = OrderedItem.objects.get_or_create(item=item, user=request.user, ordered=False)
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
    response = HttpResponse('Items have been ordered!')
    return response
