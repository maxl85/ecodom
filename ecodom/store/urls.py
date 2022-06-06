from store import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='home'),
    # path('category/<int:category_id>', views.get_category, name='category'),
    # path('product/<int:product_id>', views.view_product, name='view_product'),

    path('', views.ProductListView.as_view(), name='home'),
    path('category/<int:category_id>', views.ProductByCategory.as_view(), name='category'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='view_product'),
]