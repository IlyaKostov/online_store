from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_category_list():

    if settings.CACHE_ENABLED:
        key = 'category_list'
        cached_data = cache.get(key)
        if cached_data is None:
            cached_data = Category.objects.all()
            cache.set(key, cached_data)

        return cached_data
    return Category.objects.all()
