from store import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>', views.get_category, name='category'),
]