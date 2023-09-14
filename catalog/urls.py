from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
