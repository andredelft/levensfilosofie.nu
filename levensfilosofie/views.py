from django.shortcuts import render
from django.conf import settings

from annonces.models import Symposium
from leden.models import Member
from datetime import date


def home(request):
    today = date.today()
    upcoming_symposia = Symposium.objects.filter(date__gte=today).order_by("date")
    annonce = upcoming_symposia.filter(to_be_announced=False, canceled=False).first()
    members = Member.objects.all()

    return render(
        request,
        "index.html",
        {
            "hide_logo": True,
            "upcoming_symposia": upcoming_symposia,
            "annonce": annonce,
            "no_animation": "no_animation" in request.GET.keys(),
            "members": members,
            "photo": {
                "urls": {
                    "raw": "https://images.unsplash.com/photo-1625745450753-3c0b0678b2ae?ixid=MnwzMzE4NjN8MHwxfGFsbHx8fHx8fHx8fDE2NjM4NTkxNTA&ixlib=rb-1.2.1",
                    "full": "https://images.unsplash.com/photo-1625745450753-3c0b0678b2ae?crop=entropy&cs=tinysrgb&fm=jpg&ixid=MnwzMzE4NjN8MHwxfGFsbHx8fHx8fHx8fDE2NjM4NTkxNTA&ixlib=rb-1.2.1&q=80",
                    "regular": "https://images.unsplash.com/photo-1625745450753-3c0b0678b2ae?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMzE4NjN8MHwxfGFsbHx8fHx8fHx8fDE2NjM4NTkxNTA&ixlib=rb-1.2.1&q=80&w=1080",
                    "small": "https://images.unsplash.com/photo-1625745450753-3c0b0678b2ae?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMzE4NjN8MHwxfGFsbHx8fHx8fHx8fDE2NjM4NTkxNTA&ixlib=rb-1.2.1&q=80&w=400",
                    "thumb": "https://images.unsplash.com/photo-1625745450753-3c0b0678b2ae?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMzE4NjN8MHwxfGFsbHx8fHx8fHx8fDE2NjM4NTkxNTA&ixlib=rb-1.2.1&q=80&w=200",
                    "small_s3": "https://s3.us-west-2.amazonaws.com/images.unsplash.com/small/photo-1625745450753-3c0b0678b2ae",
                },
                "user": {
                    "name": "Ümit Yıldırım",
                    "links": {"html": {"https://unsplash.com/ja/@umityildirim"}},
                },
            },
        },
    )
