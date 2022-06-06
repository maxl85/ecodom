from msilib.schema import ListView
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = 'products'
    # extra_context = {'title': 'ЭкоДом'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'ЭкоДом'
        return context
    
    # def get_queryset(self):
    #     return Product.objects.filter(is_available=True)
    
class ProductByCategory(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        # return Product.objects.filter(category_id=self.kwargs['category_id'], is_available=True)
        return Product.objects.filter(category_id=self.kwargs['category_id'])

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = 'item'
    # pk_url_kwarg = 'product_id'




# def index(request):
#     context = {
#         'products': Product.objects.all(),
#         'title': 'ЭкоДом',
#     }
#     return render(request, "store/index.html", context)

# def get_category(request, category_id):
#     products = Product.objects.filter(category_id=category_id)
#     #categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, "store/category.html", {'products': products, 'category': category})

# def view_product(request, product_id):
#     # item = Product.objects.get(pk=product_id)
#     item = get_object_or_404(Product, pk=product_id)
#     return render(request, "store/view_product.html", {'item': item})


