"""procurement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

from workflow import views

urlpatterns = [
    url(r'^start/', views.start, name='start'),
    url(r'^requisition/', views.requisition, name='requisition'),
    url(r'^progress/', views.progress, name='progress'),
    url(r'^authorise/', views.authorise, name='authorise'),
	url(r'^requisition_authorization/', views.requisition_authorization, name='requisition_authorization'),
    url(r'^raise_req/', views.raise_req, name='raise_req'),
    url(r'^template/', views.template, name='template'),
]
