from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^message/(?P<message_id>.*)/$', views.message_retrieve, name='message_retrieve'),
]