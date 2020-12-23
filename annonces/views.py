from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from annonces.models import Symposium

# Create your views here.

class AnnonceList(ListView):
    queryset = Symposium.objects.all().prefetch_related('talk_set', 'programitem_set').order_by('-date')
    context_object_name = 'symposia'


class AnnonceDetail(DetailView):
    model = Symposium
    context_object_name = 'symposium'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program'] = self.object.programitem_set.filter(symposium=self.object).order_by('number')
        context['talks'] = self.object.talk_set.filter(symposium=self.object).order_by('number')
        return context
