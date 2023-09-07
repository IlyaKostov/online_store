from django.shortcuts import render

from catalog.models import Product
from catalog.utils import save_to_json


# Create your views here.
def home(request):
    latest_products = Product.objects.order_by('-id')[:5]

    # Вывод товаров в консоль
    for product in latest_products:
        print(f'Название: {product.product_name}, Цена: {product.purchase_price}')
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'You have new message from {name}({email}): {message}')
        save_to_json(request.POST)
    return render(request, 'catalog/contact.html')
