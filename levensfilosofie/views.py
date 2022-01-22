from django.shortcuts import redirect, render, reverse

from annonces.models import Symposium
from datetime import date

TODAY = date.today()


def home(request):
    upcoming_symposia = Symposium.objects.filter(date__gte=TODAY).order_by("date")
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
