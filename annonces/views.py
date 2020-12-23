from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from annonces.models import Symposium

# Create your views here.

class AnnonceList(ListView):
    queryset = Symposium.objects.all().prefetch_related('talk_set', 'programitem_set').order_by('date')
    context_object_name = 'symposia'
    template_name = 'annonces/list.html'

class AnnonceDetail(DetailView):
    pass
