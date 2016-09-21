"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import LoginFormView, RegisterFormView, LogoutView
from blog import views
from django.views.generic.base import RedirectView
admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='blog/')), 
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^login/$', LoginFormView.as_view(), name = "login"),
    url(r'^logout/$', LogoutView.as_view(), name = "logout"),
    url(r'^register/$', RegisterFormView.as_view(), name = "register"),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile_edit/$', views.update_profile, name="profile_edit"),
]
