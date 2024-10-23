from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist

class ArticleSerializer(serializers.ModelSerializer):
    time_for_publication = serializers.SerializerMethodField() #add new field to serializer
    #author = JournalistSerializer()
    #author = serializers.StringRelatedField() #To display the foriegn key data in string format
    class Meta:
        model = Article
        #fields = "__all__" #seralize all the fields
        #fields = ("author","title","description") #Serialize specific fields
        exclude = ("updated_at", "created_at") #Exclude Specific fields
    def get_time_for_publication(self, object): #function name should be get_{created field}
        publication_date = object.publication_date
        now = datetime.now()
        time_diff = timesince(publication_date, now)
        return time_diff
    def validate(self, data):
        """Checking the object level validation - title and description should be different"""
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description should be different")
        return data
    
    def validate_body(self, value):
        """Field-level validation to ensure the value in the body field contains 
        at least 60 characters."""
        if len(value) < 60:
            raise serializers.ValidationError("Body should have atleast 60 characters")
        return value

class JournalistSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only= True)
    class Meta:
        model = Journalist
        fields = "__all__"
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only = True)
#     updated_at = serializers.DateTimeField(read_only = True)

#     def create(self, validate_data):
#         """
#         The ** syntax is used to unpack the dictionary validate_data into 
#         keyword arguments. Each key in the validate_data dictionary should 
#         correspond to a field in the Article model. Django will automatically 
#         map those key-value pairs to the model's fields and save a new record.
#         """
#         print(validate_data)
#         return Article.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.author = validate_data.get('autor', instance.author)
#         instance.title = validate_data.get('title', instance.title)
#         instance.description = validate_data.get('description', instance.description)
#         instance.body = validate_data.get('body', instance.body)
#         instance.location = validate_data.get('location', instance.location)
#         instance.publication_date = validate_data.get('publication_date', instance.publication_date)
#         instance.active = validate_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         """Checking the object level validation - title and description should be different"""
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description should be different")
#         return data
    
#     def validate_body(self, value):
#         """Field-level validation to ensure the value in the body field contains 
#         at least 60 characters."""
#         if len(value) < 60:
#             raise serializers.ValidationError("Body should have atleast 60 characters")
#         return value