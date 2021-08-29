from . import models
from django.urls import path
from . import views

urlpatterns = [
    path('createurl/', views.createshorturl),
]