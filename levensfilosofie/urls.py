from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings

from levensfilosofie import views

urlpatterns = [
    path('', views.home, name='home'),
    path('annonces/', include('annonces.urls')),
    path('leden/', include('leden.urls'))
]

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
