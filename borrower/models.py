from django.db import models

import uuid

# Create your models here.

class BaseClass(models.Model) :

    uuid = models.SlugField(unique = True,default = uuid.uuid4)

    active_status = models.BooleanField(default = True)

    created_at = models.DateTimeField(auto_now_add = True)

    updated_at = models.DateTimeField(auto_now = True)

    class Meta :

        abstract = True

class Borrower(models.Model):

    id = models.CharField(max_length=100)

    name = models.CharField(max_length=100)

    email = models.EmailField(max_length=20)

    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)

    borrowed_date = models.DateField()

    def __str__(self) :

        return f'{self.id} {self.name}'
    
    class Meta :

         verbose_name = 'Borrower'

         verbose_name_plural = 'Borrowers'

         ordering = ['id']