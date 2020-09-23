from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.signup,name="signup"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('home',views.home,name="home"),
    path('profile',views.profile,name="profile"),
    path('details',views.details,name="details"),
    path('last',views.last,name="last"),
    path('logout',views.logout,name="logout"),
]