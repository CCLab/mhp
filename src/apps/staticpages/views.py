from django.views import generic


class ContactView(generic.TemplateView):
    template_name = 'staticpages/contact.html'
