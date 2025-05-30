from django.shortcuts import render,redirect

from django.views import View

from .forms import BorrowerForm

# Create your views here.

class borroweddateUpdateView(View) :
     
     def get(self,request,*args,**kwargs) :
          
          return render(request,'borrower/borrower-update.html')
     
     def post(self,request,*args,**kwargs) :
          
          uuid = kwargs.get('uuid')
          
          form = BorrowerForm(request.POST,request.FILES,instance = uuid)

          if form.is_valid() :
               
               form.save()

               return redirect('book')
          
          else :
               
               data = {'form':form}
               
               return render(request,'borrower/borrower-update.html',context = data)



