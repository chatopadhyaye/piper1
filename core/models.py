from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
from django.utils import six, timezone






# Create your models here.



class MyUserManager(BaseUserManager):

	def create_user(self, email, sex, first_name, last_name, day, month, year, phone, password1=None,):
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
			phone=phone
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
	userid = models.AutoField(primary_key=True, unique=True, editable=False)
	sex = models.CharField(choices=GENDER, max_length=10)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	day = models.CharField(max_length=10)
	month = models.CharField(max_length=10)
	year = models.CharField(max_length=10)
	phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
	date_joined = models.DateTimeField(default=timezone.now)


	def clean(self):
		"""
		Clean up blank fields to null
		"""
		if self.email == "":
			self.email = None


	objects = MyUserManager()


	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['sex', 'first_name', 'last_name', 'day', 'month', 'year']


	def __str__(self):              # __unicode__ on Python 2
		return self.userid


