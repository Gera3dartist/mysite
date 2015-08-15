from django.conf.urls import url
from . import views


__author__ = 'agerasym'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^reader/(?P<reader_id>[0-9]+)/$', views.comments, name='comments'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

