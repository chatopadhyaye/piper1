from django.contrib.auth.backends import ModelBackend
from .models import MyUser






class EmailOrPhoneModelBackend(ModelBackend):

    #This is a ModelBacked that allows authentication with either a username or an email address.


    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'phone': username}
        try:
            user = MyUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return MyUser.objects.get(pk=username)
        except MyUser.DoesNotExist:
            return None
