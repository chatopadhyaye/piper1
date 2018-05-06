from django import forms
from .models import MyUser


class MyUserForm(forms.ModelForm):
	
	class Meta:
		model = MyUser
		fields = ['email', 'password', 'first_name', 'last_name', 'sex', 'day', 'month', 'year']


	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = MyUser.objects.filter(email=email)
		if r.exists():
			raise  ValidationError("Email already exists")
		return email

	def save(self, commit=True):
		user = MyUser.objects.create_user(
			self.cleaned_data['email'],
			self.cleaned_data['sex'],
			self.cleaned_data['first_name'],
			self.cleaned_data['last_name'],
			self.cleaned_data['day'],
			self.cleaned_data['month'],
			self.cleaned_data['year'],
			self.cleaned_data['password'],

		)
		return user


"""
	def clean_email2(self):
		# Check that the two password entries match
		email = self.cleaned_data.get("email")
		email_r = self.cleaned_data.get("email_r")
		if email and email_r and email != email_r:
			raise forms.ValidationError("emails don't match")
		return email

"""