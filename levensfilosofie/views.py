from django.shortcuts import render

from annonces.models import Symposium
from datetime import date, timedelta

UPCOMING_DAYS = 28

def home(request):
    today = date.today()
    upcoming_symposium = Symposium.objects.filter(date__range=(today, today + timedelta(28))).order_by('date').first()

    return render(request, 'index.html', {'expand_header': True, 'upcoming_symposium': upcoming_symposium})
