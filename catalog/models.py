from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.product_name} {self.purchase_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)
        permissions = [
            (
                'set_published',
                'Can publish posts'
            )
        ]


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='имя')
    email = models.CharField(max_length=100, verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='телефон')
    message = models.TextField(verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.full_name} {self.email} {self.phone}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=5, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='имя версии')
    is_current_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product.product_name} - {self.version_name}({self.version_number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


@receiver(pre_save, sender=Version)
def update_active_versions(sender, instance, **kwargs):
    if instance.is_current_version:  # Проверяем, если версия становится активной
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_current_version=False)
