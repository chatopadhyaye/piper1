from django.conf.urls import url
from core import views as coreviews

urlpatterns = [
    url(r'^user/$', coreviews.login_user, name = "login"),
    url(r'^forgot/$', coreviews.forgot, name = "forgot"),
    url(r'^confirm/$', coreviews.confirm, name = "confirm"),
    url(r'^newpass/$', coreviews.newpass, name = "newpass"),
    
]