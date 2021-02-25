from rest_framework import status
from rest_framework.response import Response

from rest_framework import generics, permissions

from rest_framework.authentication import TokenAuthentication

from rest_framework.decorators import permission_classes

from users.api.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from users.models import Account
from rest_framework.authtoken.models import Token

# Register
class RegisterAPI(generics.GenericAPIView):
	permission_classes = []
	"""docstring for RegisterAPI"""
	serializer_class = RegisterSerializer
	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		print(user)
		
		return Response({
			"user": UserSerializer(user, context=self.get_serializer_context()).data,
			"token": Token.objects.get(user=user).key
			})
		
#Login

class LoginAPI(generics.GenericAPIView):
	permission_classes = []
	"""docstring for RegisterAPI"""
	serializer_class = LoginSerializer
	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		
		return Response({
			"user": UserSerializer(user, context=self.get_serializer_context()).data,
			"token": Token.objects.get(user=user).key
			})

class UserAPI(generics.RetrieveAPIView):
	permission_classes = [permissions.IsAuthenticated,]
	serializer_class = UserSerializer
	def get_object(self):
		return self.request.user
		












