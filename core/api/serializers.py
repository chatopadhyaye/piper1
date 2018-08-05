from rest_framework import serializers
from core.models import MyUser



class UserSerializer(serializers.ModelSerializer):
	"""docstring for UserSerializer"""

	


	class Meta:
		model = MyUser
		fields = ('email', 'password', 'username', 'sex', 'first_name', 'last_name', 'day', 'month', 'year', 'phone')
			

	def create(self, validated_data):
		user = super(UserSerializer, self).create(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

		
		