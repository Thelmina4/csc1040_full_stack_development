from django.contrib import admin
from .models import Author, Book

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)

# the next class is a better way to view
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year_published', 'isbn') # Columns to show
    list_filter = ('out_of_print', 'author') # Add a filter sidebar

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_year', 'country') # Columns to show
    list_filter = ('name', 'country') # Add a filter sidebar
    # Use 'ordering'  for sort'
    # ordering = ('id',) # The comma inside is required for a single-item tuple

# username = admin
# email = email@email.com
# pw = admin123456