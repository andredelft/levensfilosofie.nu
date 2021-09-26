from django.urls import include, path
from django.conf import settings
from django.contrib import admin

from levensfilosofie import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('annonces/', include('annonces.urls')),
    path('leden/', include('leden.urls'))
]

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
