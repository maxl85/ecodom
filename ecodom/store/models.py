from unicodedata import category
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = TreeForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name