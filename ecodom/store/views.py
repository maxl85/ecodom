from django.shortcuts import render
from .models import Category


def index(request):
    return render(request, "store/index.html", {'categories': Category.objects.all()})

def get_category(request):
    pass
