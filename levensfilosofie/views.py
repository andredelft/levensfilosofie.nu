from django.shortcuts import render
from django.conf import settings

from annonces.models import Symposium
from datetime import date


def home(request):
    today = date.today()
    upcoming_symposia = Symposium.objects.filter(date__gte=today).order_by("date")
    annonce = upcoming_symposia.filter(to_be_announced=False, canceled=False).first()

    return render(
        request,
        "index.html",
        {
            "hide_logo": True,
            "upcoming_symposia": upcoming_symposia,
            "annonce": annonce,
            "no_animation": "no_animation" in request.GET.keys(),
        },
    )
