# pages/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    birth_year = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    isbn = models.CharField(max_length=13, unique=True, null=False)  # No duplicates
    year_published = models.IntegerField()
    summary = models.TextField(blank=True)  # Optional in forms
    out_of_print = models.BooleanField(default=False)  # Default value
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)

    category = models.CharField(max_length=200, null=False, default="Fiction")
    
    # The added_by field links each book to the user who created it:
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    # https://www.computing.dcu.ie/~mscriney/csc1040/lectures/week2/2-model-introduction/