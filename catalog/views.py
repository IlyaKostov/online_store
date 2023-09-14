from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product, Contact


# Create your views here.
class ProductListView(ListView):
    model = Product


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        context_data['object_list'] = Contact.objects.all()
        return context_data


class ProductDetailView(DetailView):
    model = Product
