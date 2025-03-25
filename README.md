# Ex02 Django ORM Web Application
# Date: 24/03/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import Book  

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pages", "publication_date")

admin.site.register(Book, BookAdmin)


models.py

from django.db import models
# Create your models here.

class Book(models.Model):  
    isbn = models.CharField(max_length=20, help_text="ISBN Number")  
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=100)  
    pages = models.IntegerField()  
    publication_date = models.DateField()


```
# OUTPUT

![alt text](<Screenshot 2025-03-25 210249.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
