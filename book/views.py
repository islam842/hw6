from django.http import HttpResponse
from django.shortcuts import render
from . import models


def bookview(request):
    book = models.Book.objects.all()
    context = {
        'book_object': book
    }
    return render(request, 'book.html', context)
