from django.http import HttpResponse
from .models import Books
from django.shortcuts import render


def index(request):
    books = Books.objects.all()
    context = {
        'books': books,
        'title': 'Наименование',
    }
    return render(request, template_name='library/index.html', context=context)