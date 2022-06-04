from django.shortcuts import render
from .models import Category, Product


def index(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, "store/index.html", context)

def get_category(request):
    pass


