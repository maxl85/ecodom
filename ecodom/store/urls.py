from store import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>', views.get_category, name='category'),
    path('product/<int:product_id>', views.view_product, name='view_product'),
]