from django.conf.urls import url

from . import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^foos$', views.FoosView.as_view(), name='foo'),
]
