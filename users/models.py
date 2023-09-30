from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=30, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
