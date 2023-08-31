from django.shortcuts import render

from catalog.utils import save_to_json


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'You have new message from {name}({email}): {message}')
        save_to_json(request.POST)
    return render(request, 'catalog/contact.html')
