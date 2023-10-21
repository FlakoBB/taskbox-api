from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    username = data.get('username')
    password = data.get('password')

    if username and password:
      user = User.objects.filter(username=username).first()
      if user:
        if user.password != password:
          raise serializers.ValidationError('incorrect Password')
      else:
        raise serializers.ValidationError('User not found')
    else:
      raise serializers.ValidationError('Must include "username" and "password".')
    
    return data