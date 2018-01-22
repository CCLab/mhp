from django.conf.urls import url

from src.apps.bible import views

urlpatterns = [
    url(r'^indeks/', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>.*)', views.ShowView.as_view(), name='show'),
]
