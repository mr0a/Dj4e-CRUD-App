from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from crud.models import Make, Autos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class AutosView(LoginRequiredMixin, ListView):
    model = Autos

    def get_context_data(self, **kwargs):
        make = Make.objects.all().count()
        context = super().get_context_data(**kwargs)
        context['mc'] = make
        return context

class AutosCreate(LoginRequiredMixin, CreateView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('autos_all')

class AutosUpdate(LoginRequiredMixin, UpdateView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('autos_all')

class AutosDelete(LoginRequiredMixin, DeleteView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('autos_all')

class MakeView(LoginRequiredMixin, ListView):
    model = Make

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos_all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos_all')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos_all')

class CatsView(LoginRequiredMixin, View):
    def get(self, req):
        return HttpResponse("Hello")