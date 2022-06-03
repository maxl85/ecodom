from email.policy import default
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


def categories_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images/categories/<name>/<filename>
    return 'images/categories/{0}/{1}'.format(instance.name, filename)

class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children', verbose_name='Категория')
    image = models.ImageField(upload_to=categories_path, max_length=255, blank=True, verbose_name='Фото')

    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})


def products_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images/products/<category.name>/<filename>
    return 'images/products/{0}/{1}'.format(instance.category.name, filename)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True)
    category = TreeForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    # properties = models.TextField(blank=True, verbose_name='Характеристики')
    price = models.IntegerField(default=0, verbose_name='Цена')
    # images = models.ImageField(upload_to='images/products/%Y-%m-%d/', max_length=255)
    images = models.ImageField(upload_to=products_path, max_length=255, blank=True, verbose_name='Фото')
    is_available = models.BooleanField(default=False, verbose_name='В наличии')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Изменён')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_date']