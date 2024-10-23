"""
@api_view decorator in Django REST Framework (DRF) is used to specify which 
HTTP methods a view can handle and to ensure that the view will properly handle 
requests and responses using DRF's functionality. It's typically used with function-based 
views (FBVs) to transform them into API views that can handle requests and return serialized responses.
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView #API view class
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer

class CreateArticle(APIView):

    def get(self, request):
        articles = Article.objects.filter(active = True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListAPIView(APIView):

    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CreateJournalist(APIView):

    def get(self, request):
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(journalists, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListJournalistAPIView(APIView):

    def get_object(self, pk):
        journalist = get_object_or_404(Journalist, pk=pk)
        return journalist
    
    def get(self, request, pk):
        journalist = self.get_object(pk)
        serializer = JournalistSerializer(journalist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        journalist = self.get_object(pk)
        serializer = JournalistSerializer(journalist, data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        journalist = self.get_object(pk)
        journalist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def article_list_create_api_vew(request):
#     """
#         We are not using the Json response instead of that we are using
#         Response class provided by rest_framework
#     """
#     if request.method == "GET":
#         articles = Article.objects.filter(active = True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data) 
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# @api_view(["GET", "PUT","DELETE"])
# def article_details_api_view(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"error":{ 
#                                "code": 404,
#                                "message": "Article Not Found"

#                             }},status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    