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

class Book(models.Model):

    id = models.CharField(max_length=100)

    title = models.CharField(max_length=100)

    author = models.CharField(max_length=20)

    published_date = models.DateField()

    isbn = models.CharField(max_length=50)

    def __str__(self) :

        return f'{self.id} {self.title}'
    
    class Meta :

         verbose_name = 'Book'

         verbose_name_plural = 'Books'

         ordering = ['id']