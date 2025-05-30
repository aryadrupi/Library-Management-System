from django import forms

from .models import Book

class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = ['id', 'title','author', 'publeshed_date', 'isbn']

        widgets = {
                'id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter id'
            }),
                'title': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
                'author': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter autheor'
            }),
                'published_date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter published_date'
            }),
                'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter isbn'
            }),
        }
