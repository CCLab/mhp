from django.views import generic

from src.apps.parametrizedimage import models


class IndexView(generic.ListView):
    model = models.Card
    template_name = 'parametrizedimage/index.html'
    paginate_by = 100


class ShowView(generic.DetailView):
    model = models.Card
    template_name = 'parametrizedimage/show.html'
