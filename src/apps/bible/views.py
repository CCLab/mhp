from django.views import generic

from src.apps.bible import models


class IndexView(generic.ListView):
    model = models.Bible
    template_name = 'bible/index.html'


class ShowView(generic.TemplateView):
    template_name = 'bible/show.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        bible = models.Bible.objects.get(slug=self.kwargs['slug'])
        image_id = int(self.request.GET.get('page', 1))

        context['bible'] = bible
        context['image'] = \
            models.BiblePage.objects.get(bible=bible, ordering=image_id)

        context['next_image_exists'] = \
            models.BiblePage.objects.filter(bible=bible, ordering=image_id + 1).exists()
        context['next_image_id'] = image_id + 1

        context['previous_image_exists'] = image_id > 1
        context['previous_image_id'] = image_id - 1

        context['image_id'] = image_id
        return context
