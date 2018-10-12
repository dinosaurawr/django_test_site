"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path, reverse
from django.contrib import admin
import django

urlpatterns = [
    re_path(r'^', include('marcador.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/$', django.contrib.auth.LoginView.as_view(template_name='login.html'), name='mysite_login'),
    re_path(r'^logout/$', django.contrib.auth.LogoutView.as_view(next_page=reverse('marcador_bookmark_list')), name='mysite_logout'),
]