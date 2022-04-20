from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
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
# def product_detailed_view(request):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description,
#     #     'price': obj.price,
#     # }
#     context = {
#         "obj": obj,
#     }
#     #right practise
#     return render(request, 'products/product_detail.html', context)

#def product_create_view(request):
#    form = ProductForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#
#    context = {
#        "form": form,
#    }
#    #right practise
#    return render(request, 'products/product_create.html', context)

def product_create_view(request):
    my_form = ProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form,

    }
    return render(request, 'products/product_create.html', context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id = id)
    context = {
        "object": obj
    }
    print(obj)
    return render(request, "products/product_detail.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)# here you have passed the obj as instance for showing already exisiting values in the update form
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
    

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)