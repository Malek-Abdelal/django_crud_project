from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.

class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack   
    context_object_name = 'data'

class SnackDetailView(DetailView):
    template_name = 'snack_details.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'create_snack.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    template_name = 'update_snack.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
    success_url = reverse_lazy('snacks')

class SnackDeleteView(DeleteView):
    template_name = 'delete_snack.html'
    model = Snack
    success_url = reverse_lazy('snacks')

