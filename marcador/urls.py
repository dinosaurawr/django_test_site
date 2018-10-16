from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user , name='marcador_bookmark_user'),
    re_path(r'^create/$', views.bookmark_create, name='marcador_bookmark_create'),
    re_path(r'^edit/(?P<pk>\d+)/$', views.bookmark_edit, name='marcador_bookmark_edit'),
    re_path(r'^$', views.bookmark_list, name='marcador_bookmark_list'),
]