from django import forms

from .models import Borrower

from book.models import Book

class BorrowerForm(forms.ModelForm):

    class Meta:

        model = Borrower

        fields = ['id', 'name','email','book','borrowed_date']

        widgets = {
                'id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter id'
            }),
                'name': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
                'email': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
                'book': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book'
            }),
                'borrowed_date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter borrowed_date'
            }),
        }

book = forms.ModelChoiceField(queryset = Book.objects.filter(is_available=True),widget = forms.Select(attrs = {'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                                'required' :'required'}))

