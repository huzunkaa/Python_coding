from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from coding import views
from django.conf import settings
from django.views import static

urlpatterns = [
    path('', views.line_chart),
]
