from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.


def product_create_view(request):                                # to get form data
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # this will reset form fields after clicking submit

    context = {
        'form': form
    }

    return render(request, "product/product_create.html", context)


def product_detail_view(request):
    object = Product.objects.get(id=1)
    # context={
    #   'title':obj.title,
    #  'description':obj.description
    # }
    context = {
        'obj': object
    }
    return render(request, "product/detail.html", context)


def dynamic_lookup_view(request, my_id):
    #object = Product.objects.get(id=my_id)
    object = get_object_or_404(Product, id=id)
    context = {
        "obj": object
    }
    return render(request, "product/detail.html", context)


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
