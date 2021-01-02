from django.urls import path

from personalia.views import PersonaliaList

urlpatterns = [
    path('', PersonaliaList.as_view(), name='personalia_list')
]
