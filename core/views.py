from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages

# def home_page(request):
#     context = {
#         'items': ItemList.objects.all()
#     }
#     return render(request, 'home-page.html', context)



#
# def product_page(request, pid):
#     context = {
#         'product': ItemList.objects.get(id=pid),
#     }
#     return render(request, 'product-page.html', context)
#



class HomeView(ListView):
    model = ItemList
    paginate_by = 8
    template_name = 'home-page.html'



class ItemDetailView(DetailView):
    model = ItemList
    template_name = 'product-page.html'



def add_to_cart(request, slug):
    item = get_object_or_404(ItemList, slug=slug)
    order_item, created = OrderItemList.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = OrderList.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            messages.info(request, "This item was added to your cart.")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = OrderList.objects.create(
            user=request.user,
            ordered_date=ordered_date
        )
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect('core:product', slug=slug)



def remove_from_cart(request, slug):
    item = get_object_or_404(ItemList, slug=slug)
    order_qs = OrderList.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItemList.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "Item was removed from your cart.")
            return redirect('core:product', slug=slug)

        else:
            messages.info(request, "This item was not in your cart.")
            return redirect('core:product', slug=slug)

    else:
        messages.info(request, "You do not have any active product.")
        return redirect('core:product', slug=slug)



def checkout_page(request):
    return render(request, 'checkout-page.html')

