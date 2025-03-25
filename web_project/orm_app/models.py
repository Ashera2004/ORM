from django.db import models
# Create your models here.

class Book(models.Model):  
    isbn = models.CharField(max_length=20, help_text="ISBN Number")  
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=100)  
    pages = models.IntegerField()  
    publication_date = models.DateField()


