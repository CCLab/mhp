import copy
import collections
import urllib.parse

from django.views import generic

from src.apps.parametrizedimage import models


class IndexView(generic.ListView):
    template_name = 'parametrizedimage/index.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = models.Card.objects.all()

        for parameter in models.CARD_PARAMETERS:
            if parameter['type'] == 'string':
                if parameter['parameter_name'] in self.request.GET:
                    qs = qs.filter(**{parameter['parameter_name']: self.request.GET[parameter['parameter_name']]})
            elif parameter['type'] == 'float':
                if '%s_min' % parameter['parameter_name'] in self.request.GET:
                    qs = qs.filter(**{
                        '%s__gte' % parameter['parameter_name']:
                            float(self.request.GET['%s_min' % parameter['parameter_name']])})
                if '%s_max' % parameter['parameter_name'] in self.request.GET:
                    qs = qs.filter(**{
                        '%s__lte' % parameter['parameter_name']:
                            float(self.request.GET['%s_max' % parameter['parameter_name']])})
            else:
                assert(False)
        return qs

    def get_criteria(self):
        def get_url_if_removed(query_dict, parameter_name):
            new_dict = copy.copy(query_dict)
            del new_dict[parameter_name]
            url = urllib.parse.urlencode(collections.OrderedDict(new_dict))
            return '?%s' % url

        criteria = []

        for parameter in models.CARD_PARAMETERS:
            if parameter['type'] == 'string':
                if parameter['parameter_name'] in self.request.GET:
                    criteria.append({
                        'parameter_name': parameter['parameter_name'],
                        'as_text': "%s jest równe %s" % (
                            parameter['parameter_name_human'],
                            self.request.GET[parameter['parameter_name']]),
                        'url_if_removed': get_url_if_removed(
                            self.request.GET,
                            parameter['parameter_name'])
                    })
            elif parameter['type'] == 'float':
                if '%s_min' % parameter['parameter_name'] in self.request.GET:
                    criteria.append({
                        'parameter_name': parameter['parameter_name'],
                        'as_text': "%s jest większe lub równe %s" % (
                            parameter['parameter_name_human'],
                            self.request.GET['%s_min' % parameter['parameter_name']]),
                        'url_if_removed': get_url_if_removed(
                            self.request.GET,
                            '%s_min' % parameter['parameter_name'])
                    })
                if '%s_max' % parameter['parameter_name'] in self.request.GET:
                    criteria.append({
                        'parameter_name': parameter['parameter_name'],
                        'as_text': "%s jest mniejsze lub równe %s" % (
                            parameter['parameter_name_human'],
                            self.request.GET['%s_max' % parameter['parameter_name']]),
                        'url_if_removed': get_url_if_removed(
                            self.request.GET,
                            '%s_max' % parameter['parameter_name'])
                    })
            else:
                assert(False)
        return criteria

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['card_parameters'] = models.CARD_PARAMETERS
        context['criteria'] = self.get_criteria()
        return context


class ShowView(generic.DetailView):
    model = models.Card
    template_name = 'parametrizedimage/show.html'
