from django.contrib import admin

from catalog.models import Product, Category, Contact


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'purchase_price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Contact)
