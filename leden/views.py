from django.views.generic import ListView

from leden.models import Member

# Create your views here.

class MemberList(ListView):
    model = Member
    ordering = ['last_name', 'first_name', 'key']
    context_object_name = 'members'
