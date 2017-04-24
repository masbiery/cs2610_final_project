from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^submitted/', views.message_submitted, name='message_submitted'),
]