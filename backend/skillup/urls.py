"""skillup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from main.views import auth, pages

urlpatterns = [
    url(r'^signin/', auth.signin, name='signin'),
    url(r'^signup/', auth.signup, name="signup"),
    url(r'^signout/', auth.signout, name='signout'),
    url(r'^profile', pages.profile, name='profile'),
    url(r'^categories/(?P<name>.+)/', pages.categories, name='categories'),
    url(r'^details/(?P<id>\d+)', pages.details, name='details'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', pages.index, name="index"),
]
