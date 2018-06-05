# -*- coding: utf-8 -*-
from django.urls import path
from users import views
app_name = 'users'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
