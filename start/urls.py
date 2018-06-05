# -*- coding: utf-8 -*-
from django.urls import path
from start import views
app_name = 'start'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
