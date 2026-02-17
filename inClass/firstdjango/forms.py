from django.forms import ModelForm, ValidationError
from .models import Author, Book

# class Bookform(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'year_published', 'author']

class Authorform(ModelForm):
    
    class Meta:
        model = Author
        # note how id is left out, that is on purpose
        # people should have the option to make their own id
        # django will automatically take care of the ids for us
        fields = ['name', 'birth_date', 'genre']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # let's say we don't like James
        if "JAMES" in name.upper():
            raise ValidationError("No james allowed") 
        return name
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        # this is wrong
        if birth_date.year < 1900:
            raise ValidationError("No james allowedAothrs must be borm after 1900")    
        return birth_date

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        genre = cleaned_data.get('genre')
        
        if name and genre:
            if name.upper() == "AGATHA CHRISTIE" and genre.lower() != "mystery":
                raise ValidationError("AGATHA CHRISTIE is a mystery writer")
        return cleaned_data
            
    def save(self, commit=True):
        author = super().save(commit=False)# create an Author instance but don't save to DB yet, just keep in memory
        author.created_by = "Mike"  # set the created_by field to a default value
        if commit:
            author.save()  # now save to the database
        return author
