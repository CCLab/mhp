from django.views import generic

from src.apps.bible import models


class IndexView(generic.ListView):
    model = models.Bible
    template_name = 'bible/index.html'


class ShowView(generic.TemplateView):
    template_name = 'bible/show.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['image'] = models.BiblePage
        return context
