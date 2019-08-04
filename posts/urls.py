from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/index$', login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^logout/$', views.logout, name="logout"),
    url(r'^add/$', views.add_new_post, name='add'),
    url(r'^board/$', views.add_new_post, name='board')
]