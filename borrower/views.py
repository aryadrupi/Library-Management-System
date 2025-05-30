from django.views import View

from django.shortcuts import render, redirect, get_object_or_404

from .models import Borrower

from .forms import BorrowerForm

# Create your views here.

class BorrowerListView(View):

    def get(self,request,args,*kwargs):

        borrowers = Borrower.objects.get('book')

        return render(request, 'borrower_list.html', {'borrowers': borrowers})


class BorrowerCreateView(View):

    def get(self,request,args,*kwargs):

        form = BorrowerForm()

        return render(request, 'add_borrower.html', {'form': form})

    def post(self,request,args,*kwargs):

        form = BorrowerForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('borrower_list')
        
        return render(request, 'add_borrower.html', {'form': form})


class BorrowerDetailView(View):

    def get(self,request,args,*kwargs):

       pk= kwargs.get('pk')

       borrower = get_object_or_404(Borrower, pk=pk)

       return render(request, 'borrower_detail.html', {'borrower': borrower})


class BorrowerUpdateView(View):

    def get(self,request,args,*kwargs ):

        pk= kwargs.get('pk')

        borrower = get_object_or_404(Borrower, pk=pk)

        form = BorrowerForm(instance=borrower)

        return render(request, 'borrower_date.html', {'form': form})

    def post(self,request,args,*kwargs):

        pk= kwargs.get('pk')

        borrower = get_object_or_404(Borrower, pk=pk)

        form = BorrowerForm(request.POST, instance=borrower)

        if form.is_valid():

            form.save()

            return redirect('borrower_list')
        
        return render(request, 'borrower_date.html', {'form': form})