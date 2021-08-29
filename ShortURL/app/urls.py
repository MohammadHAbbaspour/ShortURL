from . import models
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('createurl/', views.createshorturl),
    # re_path(r'[aA-zZ]*[0-9]*/', views.redirect_url),
]