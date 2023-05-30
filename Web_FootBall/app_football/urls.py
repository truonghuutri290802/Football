from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('premierleague/',views.premierleague,name="premierleague"),
    path('laliga/',views.laliga,name="laliga"),
    path('bundesliga/',views.bundesliga,name="bundesliga"),
]