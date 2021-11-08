from django.shortcuts import render

from annonces.models import Symposium
from datetime import date

TODAY = date.today()


def home(request):
    upcoming_symposia = Symposium.objects.filter(date__gte=TODAY).order_by(
        "date"
    )

    return render(
        request,
        "index.html",
        {"hide_logo": True, "upcoming_symposia": upcoming_symposia},
    )
