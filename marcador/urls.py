from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user , name='marcador_bookmark_user'),
    re_path(r'^$', views.bookmark_list, name='marcador_bookmark_list'),
]