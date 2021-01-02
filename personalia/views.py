from django.views.generic import ListView

from personalia.models import Member

# Create your views here.

class PersonaliaList(ListView):
    model = Member
    ordering = ['last_name', 'first_name', 'key']
    context_object_name = 'members'
