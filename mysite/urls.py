from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from quickstart import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^', include('snippets.urls')),
)

