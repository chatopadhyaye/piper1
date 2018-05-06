from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
#import uuid
from django.utils import six, timezone


# Create your models here.



class MyUserManager(BaseUserManager):

	def create_user(self, email, sex, first_name, last_name, day, month, year, password1=None,):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			sex=sex,
			first_name=first_name,
			last_name=last_name,
			day=day,
			month=month,
			year=year,
		)

		user.set_password(password1)
		user.save(using=self._db)
		return user





GENDER = (
   ('male', 'Male'),
   ('female', 'Female')
)




class MyUser(AbstractBaseUser):
	email = models.EmailField(max_length=50, unique=True)
	userid = models.AutoField(primary_key=True, unique=True, editable=False)
	sex = models.CharField(choices=GENDER, max_length=10)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	day = models.CharField(max_length=10, default='01')
	month = models.CharField(max_length=10, default='january')
	year = models.CharField(max_length=10, default='1995')
	date_joined = models.DateTimeField(default=timezone.now)



	objects = MyUserManager()


	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['sex', 'first_name', 'last_name', 'day', 'month', 'year']


	def __str__(self):              # __unicode__ on Python 2
		return self.userid











"""
class cred(models.Model):
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)


GENDER = (
   ('male', 'Male'),
   ('female', 'Female')
)


class profile(models.Model):
	userid = models.UUIDField(primary_key=True, editable=False)
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	bdate = models.DateField()
	sex = models.CharField(choices=GENDER, max_length=10)
"""