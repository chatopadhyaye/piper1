from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
from django.utils import six, timezone
import uuid

#imports to create auth token for users when they sign up
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




# Create your models here.



class MyUserManager(BaseUserManager):

	def create_user(self, email, sex, first_name, last_name, day, month, year, phone, username, password1=None,):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			if not phone:
				raise ValueError('Users must have an email or phone no.')


		user = self.model(
			email=email,
			sex=sex,
			first_name=first_name,
			last_name=last_name,
			day=day,
			month=month,
			year=year,
			phone=phone,
			username=username
		)

		user.set_password(password1)
		user.save(using=self._db)
		return user





GENDER = (
   ('male', 'Male'),
   ('female', 'Female')
)




class MyUser(AbstractBaseUser):
	email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
	#userid = models.AutoField(unique=True, editable=False)
	userid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	sex = models.CharField(choices=GENDER, max_length=10)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	day = models.CharField(max_length=10)
	month = models.CharField(max_length=10)
	year = models.CharField(max_length=10)
	phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
	date_joined = models.DateTimeField(default=timezone.now)
	username = models.CharField(primary_key=True, max_length=15, unique=True)
	is_active = models.BooleanField(default=True)


	def clean(self):
		"""
		Clean up blank fields to null
		"""
		if self.email == "":
			self.email = None


	objects = MyUserManager()


	USERNAME_FIELD='username'
	REQUIRED_FIELDS=['sex', 'first_name', 'last_name', 'day', 'month', 'year']


	def __str__(self):              # __unicode__ on Python 2
		return self.userid







#Exclusive for restframework authtoken
#creates auth Token for user when a user signup
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)




