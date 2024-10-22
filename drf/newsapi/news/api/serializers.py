from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)

    def create(self, validate_data):
        """
        The ** syntax is used to unpack the dictionary validate_data into 
        keyword arguments. Each key in the validate_data dictionary should 
        correspond to a field in the Article model. Django will automatically 
        map those key-value pairs to the model's fields and save a new record.
        """
        print(validate_data)
        return Article.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.author = validate_data.get('autor', instance.author)
        instance.title = validate_data.get('title', instance.title)
        instance.description = validate_data.get('description', instance.description)
        instance.body = validate_data.get('body', instance.body)
        instance.location = validate_data.get('location', instance.location)
        instance.publication_date = validate_data.get('publication_date', instance.publication_date)
        instance.active = validate_data.get('active', instance.active)