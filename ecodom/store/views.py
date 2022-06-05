from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request):
    context = {
        'products': Product.objects.all(),
        'title': 'ЭкоДом',
    }
    return render(request, "store/index.html", context)

def get_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    #categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, "store/category.html", {'products': products, 'category': category})

def view_product(request, product_id):
    # item = Product.objects.get(pk=product_id)
    item = get_object_or_404(Product, pk=product_id)
    return render(request, "store/view_product.html", {'item': item})


