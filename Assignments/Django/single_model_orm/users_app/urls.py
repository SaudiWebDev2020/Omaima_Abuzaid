from django.urls import path   
from django.urls.conf import include
from . import views
urlpatterns = [
    path('', views.index),
    path('new_user', views.new_user),
    
]