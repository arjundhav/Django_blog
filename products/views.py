from random import randrange
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm

from .models import Product
# Create your views here.

def product_create_view(request):                            # to get form data
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # this will reset form fields after clicking submit

    context = {
        'form': form
    }

    return render(request, "product/product_create.html", context)


def product_detail_view(request):
    # obj = Product.objects.get(id=15)
    # context={
    #    'title':obj.title,
    #   'description':obj.description
    #  }
    
    obj = get_object_or_404(Product, id=18)
    context = {
        "object": obj
    }
    return render(request, "product/product_details.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_delete_view(request):
    object = get_object_or_404(Product, id=id)
    if request.method == "POST":
        # confirming delete
        object.delete()
    context = {
        "obj": object
    }
    return render(request, "product/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()   #list of objects
    context = {
         'object_list':queryset
    }
    return render(request, 'product/product_list.html', context)
