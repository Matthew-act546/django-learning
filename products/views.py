from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.
# def product_create_view(request):
#     """Creating a product views"""
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#     context = {
#         'form': my_form,
#     }
#     return render(request, "product/product_create.html", context)

# def product_create_view(request):
#     """Creating a product views"""
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {}
#     return render(request, "product/product_create.html", context)


def product_create_view(request):
    """Creating a product views"""
    initial_data = {
        'title': 'this is a new title',
    }
    # obj = Product.objects.get()
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("./")
    context = {
        'form': form,
    }
    return render(request, "product/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'obj': obj,
    }
    return render(request, "product/detail.html", context)

def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    
    context = {
        'obj': obj,
    }
    return render(request, "product/detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        'obj': obj,
    }
    return render(request, "product/detail_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        'object_list': queryset,
    }
    return render(request, "product/product_list.html", context)



# obj = Product.objects.get(id=my_id)
# try: 
#     obj = Product.objects.get(id=my_id)
# except Product.DoesNotExist:
#     raise Http404