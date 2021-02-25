from rest_framework import serializers

from users.models import Account

from django.contrib.auth import authenticate

#User Ser
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id', 'username', 'email', 'profile_picture')


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only':True}}

		def create(self, validated_data):
			user = Account.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

			return user



class LoginSerializer(serializers.Serializer):

	username = serializers.CharField()
	password = serializers.CharField()
	"""docstring for LoginSerializer"""
	def validate(self, data):
		user = authenticate(**data)
		if user and user.is_active:
			return user
		raise serializers.ValidationError("Incorrect Credentials")