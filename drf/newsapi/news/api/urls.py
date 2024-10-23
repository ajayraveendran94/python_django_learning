from django.urls import path
from news.api.views import (CreateArticle, 
                            ListAPIView,
                            CreateJournalist,
                            ListJournalistAPIView)
# from news.api.views import (article_details_api_view, 
#                             article_list_create_api_vew)


urlpatterns = [
    path("articles/", CreateArticle.as_view(), name= "article_list"),
    path("article/<int:pk>", ListAPIView.as_view(), name= "article_view"),
    path("journalists/", CreateJournalist.as_view(), name= "journalist_list"),
    path("journalist/<int:pk>", ListJournalistAPIView.as_view(), name= "journalists_view")
    # path("articles/", article_list_create_api_vew, name= "article_list"),
    # path("article/<int:pk>", article_details_api_view, name= "article_view")
]
