from django.conf.urls import url

from src.apps.parametrizedimage import views

urlpatterns = [
    url(r'^indeks/', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>.*)', views.ShowView.as_view(), name='show'),
]
