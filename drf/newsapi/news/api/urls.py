from django.urls import path
from news.api.views import (article_details_api_view, 
                            article_list_create_api_vew)

urlpatterns = [
    path("articles/", article_list_create_api_vew, name= "article_list"),
    path("article/<int:pk>", article_details_api_view, name= "article_view")
]
