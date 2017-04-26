from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<message_id>.*)/$', views.message_retrieve, name='message_retrieve'),
]