from django.conf.urls import url
from . import views

# namespace/ just in case url name is the same / if lots of apps
app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
