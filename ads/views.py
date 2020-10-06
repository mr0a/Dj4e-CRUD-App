#from django.shortcuts import render
from ads.owner import OwnerListView, OwnerUpdateView, OwnerCreateView, OwnerDeleteView, OwnerDetailView
from ads.models import Articles
from django.views import View
from django.urls import reverse_lazy

# Create your views here.
class AdsIndex(OwnerListView):
    '''Same'''
    template_name = 'ads/article_list.html'

class AdsDetail(OwnerDetailView):
    model = Articles

class AdsCreate(OwnerCreateView):
    model = Articles
    fields = ['title', 'price', 'text' ]
    success_url = reverse_lazy('ads:all')

class AdsUpdate(OwnerUpdateView):
    model = Articles
    fields = ['title', 'price', 'text' ]
    success_url = reverse_lazy('ads:all')

class AdsDelete(OwnerDeleteView):
    model = Articles
    success_url = reverse_lazy('ads:all')