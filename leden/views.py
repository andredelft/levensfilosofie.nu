from django.views.generic import ListView

from leden.models import Member


class MemberList(ListView):
    model = Member
    context_object_name = "members"
    queryset = Member.objects.filter(hidden=False)
