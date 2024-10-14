from django.urls import path
#from .views import ProductDetailView, ProductListView
from .views import (manufacturer, manufacture, manufacture_detail, 
                    product_list, product_detail)

urlpatterns=[
    path("products/", product_list, name = "prodcut_list"),
    path("products/<int:pk>", product_detail, name = "prodcut_detail"),
    path("manufacturer/<str:status>", manufacturer, name = "manufacturer_detail"),
    path("manufactures/", manufacture, name = "manufacturer_list"),
    path("manufacture_detail/<int:pk>", manufacture_detail, name = "manufacture_detail"),
    # path("", ProductListView.as_view(), name="product-list"),
    # path("products/<int:pk>/", ProductDetailView.as_view(), name="product-details")
]