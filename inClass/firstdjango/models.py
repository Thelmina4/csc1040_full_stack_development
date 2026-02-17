#  firstdjango/models.py

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# functions for classes
# called in books to get the current year
# https://stackoverflow.com/questions/49051017/year-field-in-django
def current_year():
    return datetime.date.today().year

# called in books to get the current year
def max_value_current_year():
    return MaxValueValidator(current_year())

# Create your MODELS here.
# test model:
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    # not the null = true, this is because there could be different inputs
    # the database can't just make a new column for every wording
    # null=True, blank=Tru
    genre = models.CharField(max_length=100, default="True")

    created_by = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
# Author.object.create(name="J.K.Rowling", birth_date="1965-07-31", genre="fantasy")

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    # don't like unbounded text. this optimised the database
    title = models.CharField(max_length=200, null=False)

    isbn = models.CharField(max_length=13,
                            unique=True,
                            blank=True,
                            null=True)  # No duplicates
    # there is a list of data types that you can use
    genre = models.CharField(max_length=100, default="Fiction")
    num_pages = models.IntegerField()
    date_published = models.DateField()
    out_of_print = models.BooleanField(default=False)  # Default value
    year = models.IntegerField(default=current_year,
                               validators=[MinValueValidator(1000), max_value_current_year()])
    # can't do a PhoneNumberField()
    # AttributeError: module 'django.db.models' has no attribute 'PhoneNumberField'  
    # phone_number = models.PhoneNumberField()

    # IMPORTANT
    # next line links the 2 classes 
    # {{book.author.name}} used in book_detail.html
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    synopsis = models.TextField(blank=True)

    # With Django models
    def get_books(request):
        books = Book.objects.filter(year_published__gt=1950)
        # books is a list of Book objects
        # Access fields by name: books[0].title ✓

    def __str__(self):
        return self.title
    
# if __name__ == "__main__":
#     print(type(current_year()))