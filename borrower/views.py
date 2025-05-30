from django.shortcuts import render,redirect

from django.views import View

from .forms import BorrowerForm

from django.views.generic.edit import CreateView

from .models import Borrower

from .forms import BorrowerForm

from django.views.generic import DetailView

from django.shortcuts import get_object_or_404

from .models import Borrower

class BorrowerCreateView(CreateView):

    model = Borrower

    form_class = BorrowerForm

    template_name = 'add_borrower.html'

    success_url = redirect('borrower_list')  

class BorrowerUpdateDateView(View):

    model = Borrower

    fields = ['borrowed_date']

    template_name = 'update_borrowed_date.html'

    success_url = redirect('borrower_list')           
          
class BorrowerDetailView(DetailView):

    model = Borrower

    template_name = 'borrower_detail.html'

    context_object_name = 'borrower'

    def get_object(self):

        return get_object_or_404(Borrower, pk=self.kwargs.get('pk'))




