from django.urls import path

from annonces.views import AnnonceList

urlpatterns = [
    path('', AnnonceList.as_view(), name='announcement_list'),
]
