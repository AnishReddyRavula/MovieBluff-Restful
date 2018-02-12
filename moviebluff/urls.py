"""moviebluff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from movies.views import CreateView
from movies.views import DetailsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',  CreateView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)$', DetailsView.as_view(), name='details'),
]
