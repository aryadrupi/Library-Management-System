from django.shortcuts import render

from django.views import View

from .models import Book

# Create your views here.

class HomeView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'book/home.html')
    
class BookView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'book/book.html')
    
class BorrowerView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'book/borrower.html')

class BookListView(View):

    def get(self,request,*args,**kwargs):

        rentals = Book.objects.all()

        return render(request,'book/book-list.html')