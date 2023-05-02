from django.shortcuts import render
from django.views import View
from .models import Product


# Create your views here.
def home(request):
    return render(request, "online/home.html")

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        return render(request, "online/category.html",locals())