from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductForm
from .models import Product

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {}) #String of HTML code
def contacts_view(request, *args, **kwargs):
    return render(request, 'contacts.html', {}) #String of HTML code
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 23,
        "my_list": [123,321,123, "abc"]
    }
    return render(request, 'about.html', my_context)
def product_detailed_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    # }
    context = {
        "obj": obj,
    }
    #right practise
    return render(request, 'products/product_detail.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form,
    }
    #right practise
    return render(request, 'products/product_create.html', context)