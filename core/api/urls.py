from django.conf.urls import url, include
from django.contrib import admin
from core.api import views





urlpatterns = [
    url(r'^usersignup/$', views.user_signup.as_view(), name = "user_signup"),
    url(r'^userlogin/$', views.user_login.as_view(), name = "user_login"),
    url(r'^check_token/$', views.check_token.as_view(), name = "check_token"),
    url(r'^check_username/$', views.check_username.as_view(), name = "check_username"),
    url(r'^check_username_list/$', views.check_username_list.as_view(), name = "check_username_list"),
]