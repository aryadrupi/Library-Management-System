from django.urls import path

from .views import BorrowerCreateView,BorrowerDetailView,BorrowerUpdateDateView

urlpatterns = [

    path('borrowers/add/', BorrowerCreateView.as_view(), name='add_borrower'),

    path('borrower/<int:pk>/', BorrowerDetailView.as_view(), name='borrower_detail'),

    path('borrower/<int:pk>/update-date/', BorrowerUpdateDateView.as_view(), name='update_borrowed_date'),
]
