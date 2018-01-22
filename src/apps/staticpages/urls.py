from django.conf.urls import url

from src.apps.staticpages import views

urlpatterns = [
    url(r'^kontakt/', views.ContactView.as_view(), name='contact'),
]
