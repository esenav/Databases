from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'payment$', views.payment, name='payment'),
    url(r'template$', views.template, name='template'),
    url(r'$', views.main, name='main'),
]
