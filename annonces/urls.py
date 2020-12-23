from django.urls import path

from annonces.views import AnnonceList, AnnonceDetail

urlpatterns = [
    path('', AnnonceList.as_view(), name='announcement_list'),
    path('<slug:slug>', AnnonceDetail.as_view(), name='announcement_detail')
]
