from django.shortcuts import render

from catalog.models import Product, Contact
from catalog.utils import save_to_json


# Create your views here.
def home(request):
    context = {
        'objects_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contact(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'You have new message from {name}({email}): {message}')
        save_to_json(request.POST)
    return render(request, 'catalog/contact.html', {'contacts': contacts})


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)
