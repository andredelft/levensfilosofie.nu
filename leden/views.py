from django.views.generic import ListView

from leden.models import Member


class MemberList(ListView):
    model = Member
    ordering = ['last_name', 'first_name']
    context_object_name = 'members'
