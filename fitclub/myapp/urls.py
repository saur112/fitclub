from django.urls import path,include
from . import views



urlpatterns = [

    path('url/task/', views.index),

]