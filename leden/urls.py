from django.urls import path

from leden.views import MemberList

urlpatterns = [
    path('', MemberList.as_view(), name='member_list')
]
