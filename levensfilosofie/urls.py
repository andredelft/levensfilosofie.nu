from django.urls import include, path
from django.contrib import admin
from django.conf import settings

from levensfilosofie import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("annonces/", include("annonces.urls")),
    path("leden/", include("leden.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
