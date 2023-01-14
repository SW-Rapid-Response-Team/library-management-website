from django.db import models
from isbn_field import ISBNField

class Book(models.Model):
    subject = models.CharField(max_length=64)
    isbn = ISBNField()
    author = models.CharField(max_length=64)
    #category # choice 
    #count 
    register_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# Create your models here.
