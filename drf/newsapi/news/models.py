from django.db import models

# Create your models here.

class Journalist(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)

    def __str__(self):
        return f"{self.first_name}"

class Article(models.Model):
    """
    auto_now updates the field value every time the instance is saved, 
    while auto_now_add sets the field value only when the instance is created.
    """
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.author} {self.title}"



