from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]