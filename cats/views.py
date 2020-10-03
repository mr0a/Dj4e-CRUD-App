#from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cats.models import Cats, Breeds
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CatsView(LoginRequiredMixin, ListView):
    model = Cats

    def get_context_data(self, **kwargs):
        bc = Breeds.objects.all().count()
        context = super().get_context_data(**kwargs)
        context['bc'] = bc
        return context

class CatsCreate(LoginRequiredMixin, CreateView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats_list')

class CatsUpdate(LoginRequiredMixin, UpdateView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats_list')

class CatsDelete(LoginRequiredMixin, DeleteView):
    model = Cats
    fields = '__all__'
    success_url = reverse_lazy('cats_list')

class BreedsView(LoginRequiredMixin, ListView):
    model = Breeds

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BreedsCreate(LoginRequiredMixin, CreateView):
    model = Breeds
    fields = '__all__'
    success_url = reverse_lazy('cats_list')

class BreedsUpdate(LoginRequiredMixin, UpdateView):
    model = Breeds
    fields = '__all__'
    success_url = reverse_lazy('breeds_list')

class BreedsDelete(LoginRequiredMixin, DeleteView):
    model = Breeds
    fields = '__all__'
    success_url = reverse_lazy('cats_list')
