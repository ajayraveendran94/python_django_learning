# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    #data = {"products": list(products.values("pk", "name"))}
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk = pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "image": product.image.url,
            "price": product.price,
            "shippping_cost": product.shipping_cost,
            "quantity": product.quantity,
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code": 404,
                "message": "product not found"
            }
        }, status=404)
    return response

#My Solution
def manufacturer(request, status):
    try:
        if status == "true":
            manufacturer = Manufacturer.objects.filter(active = True)
        else:
            manufacturer = Manufacturer.objects.all()
        data_set = []
        if manufacturer:
            for manufact in manufacturer:
                data = { "manufacturer": {
                    "name": manufact.name,
                    "location": manufact.location,
                    "status": manufact.active,
                    "products": list(manufact.products.values())
                }}
                data_set.append(data)
        print(data_set)
        response = JsonResponse(data_set,safe= False)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code": 404,
                "message": "Manufacturer not found"
            }
        }, status=404)
    return response

#Answer
def manufacture(request):
    manufacturers = Manufacturer.objects.all()
    data = {"manufacturer": list(manufacturers.values())}
    response = JsonResponse(data)
    return response

def manufacture_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.filter(active=True).get(pk = pk)
        manufacture_products = manufacturer.products
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "status": manufacturer.active,
            "products": list(manufacture_products.values())
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error":{
                "code": 404,
                "message": "Manufacturer not found"
            }
        }, status=404)
    return response


# Create your views here.

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"