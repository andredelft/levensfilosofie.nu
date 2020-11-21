from django.urls import path
from django.views.generic import RedirectView

from levensfilosofie import views

urlpatterns = [
    path('', views.home, name = 'home')
]
