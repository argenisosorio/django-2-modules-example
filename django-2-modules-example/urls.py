# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('start.urls')),
    path('users', include('users.urls')),
    path('projects', include('projects.urls')),
]
