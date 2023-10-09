from django.views import generic


from .models import Monster

# Create your views here.


class MonsterListView(generic.ListView):
    model = Monster
    ordering = ["name"]


class MonsterDetailView(generic.DetailView):
    model = Monster
