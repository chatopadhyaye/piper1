from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from core.models import MyUser
import json




#sign up and create user
class user_signup(APIView):

	permission_classes = (permissions.AllowAny,)


	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(request.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# Login user and send token upon successful authentication
class user_login(ObtainAuthToken):
	

	permission_classes = (permissions.AllowAny,)


	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			'token': token.key,
			'username': user.username,
			'email': user.email
		})


#checks for valid token		
class check_token(APIView):
	
	def get(self, request):
		return Response(status=status.HTTP_200_OK)
		


# not in use
class check_username(APIView):

	permission_classes = (permissions.AllowAny,)
	
	def post(self, request):

		username = request.data['username']

		if MyUser.objects.filter(username=username).exists():
			return Response(status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_200_OK)
		

#not in use
class check_username_list(APIView):

	permission_classes = (permissions.AllowAny,)
	
	def post(self, request):


		j = request.data["usernames"]
		username = json.loads(j)

		x = []
		count = 0
		for i in username:
			if count > 9:
				break
			if MyUser.objects.filter(username=i).exists():
				continue
			else:
				x.append(i)
				count += 1

		return Response(x, status=status.HTTP_200_OK)


		
