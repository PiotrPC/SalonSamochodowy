# from django.shortcuts import render
#
# # Create your views here.
# def cars(request):
#     return render(request, 'cars.html')

from django.views.generic.detail import DetailView
from .models import book

class BookDeatilView(DetailView)
    model = BookDeatilView
    template_name = 'ai_app/book_detail.html'
    context_object_name = 'book'