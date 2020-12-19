from django.urls import include, path
from django.views.generic import RedirectView

from levensfilosofie import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aankondigingen/', include('aankondigingen.urls'))
]
