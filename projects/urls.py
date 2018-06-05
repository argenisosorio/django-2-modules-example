# -*- coding: utf-8 -*-
from django.urls import path
from projects import views
app_name = 'projects'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
