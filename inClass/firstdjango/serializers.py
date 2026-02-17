from os import read
#need to go to settings and finish it
from rest_framework import serialisers
from .models import Author, Book

class AuthorSerializer(serialisers.HyperLinkedModelSerializer):
    class Meta:
        model = Author
        # need to make sure that the fieldsnames match up corretly
        fields = ['id', 'name', 'birth_dates', 'genre', 'created_by']

    def validate_name()
        # need to set up a view for restframework