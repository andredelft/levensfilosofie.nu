from django.views.generic import ListView, DetailView

from annonces.models import Symposium

# Create your views here.


class AnnonceList(ListView):
    model = Symposium
    ordering = "-date"
    context_object_name = "symposia"
    queryset = Symposium.objects.filter(to_be_announced=False)


class AnnonceDetail(DetailView):
    model = Symposium
    context_object_name = "symposium"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["program"] = self.object.programitem_set
        context["talks"] = self.object.talk_set.order_by("pk")
        return context
