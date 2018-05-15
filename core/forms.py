from django import forms
from .models import MyUser



class MyUserForm(forms.ModelForm):
	
	class Meta:
		model = MyUser
		fields = ['email', 'password', 'first_name', 'last_name', 'sex', 'day', 'month', 'year', 'phone']



	def clean_email(self):
		if self.cleaned_data['email'] is not None:
			email = self.cleaned_data['email'].lower()
			e = MyUser.objects.filter(email=email)
			if e != "":
				if e.exists():
					raise  ValidationError("Email already exists")
				return email


	def clean_phone(self):
		phone = self.cleaned_data['phone']
		if phone is not None:
			p = MyUser.objects.filter(phone=phone)
			if p != "":
				if p.exists():
					raise ValidationError("Phone no. already exists")
				return phone




	def save(self, commit=True):
		user = MyUser.objects.create_user(
			self.cleaned_data['email'],
			self.cleaned_data['sex'],
			self.cleaned_data['first_name'],
			self.cleaned_data['last_name'],
			self.cleaned_data['day'],
			self.cleaned_data['month'],
			self.cleaned_data['year'],
			self.cleaned_data['phone'],
			self.cleaned_data['password'],
		)
		return user






"""
	def clean_email_phone(self):
		logid = self.cleaned_data['logid'].lower()
		if '@'in logid:
			r = MyUser.objects.filter(email=logid)
			if r.exists():
				raise ValidationError("Email already exists")
			return logid
		else:
			p = MyUser.objects.filter(phone=logid)
			if p.exists():
				raise ValidationError("Phone no. already exists")
			return logid
"""
