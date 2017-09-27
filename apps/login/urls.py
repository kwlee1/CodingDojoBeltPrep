from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register',views.register),
    url(r'^success',views.success),
    url(r'^login',views.login),
    url(r'^logout',views.logout),
    url(r'^users/(?P<id>[0-9]+)$',views.users, name='users'),
    url(r'^message',views.message),
]