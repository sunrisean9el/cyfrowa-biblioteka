from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
import re

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year']

    def clean_author(self):
        author = self.cleaned_data['author']
        if any(char.isdigit() for char in author):
            raise forms.ValidationError("Imię autora nie może zawierać cyfr.")
        return author

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = datetime.date.today().year
        if year <= 0:
            raise forms.ValidationError("Rok musi być liczbą dodatnią.")
        if year > current_year:
            raise forms.ValidationError(f"Rok nie może być większy niż {current_year}.")
        return year

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']