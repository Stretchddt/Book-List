from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# Create your views here.
class BookList(ListView):
    model = Book
    context_object_name = 'books'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get('search') or ''
        if search_text:
            context['books'] = context['books'].filter(title__icontains=search_text)
            
        context['search_text'] = search_text
        return context
    
class CreateBook(CreateView):
    model = Book
    fields = ['title', 'description', 'author']
    success_url = reverse_lazy('book_list')
    
class UpdateBook(UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'completed']
    success_url = reverse_lazy('book_list')

class DeleteBook(DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')