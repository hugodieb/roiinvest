from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth.password_validation import validate_password
from .utils.validators import cpf_check

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    ModuleNotFoundError = Profile
    fields = ['birth_date', 'age', 'cpf', 'phone', 'avatar']

  def validate_cpf(self, value):
    return cpf_check(value)
  
class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer

  class Meta:
    model = User
    fields = ['id', 'email', 'username', 'subscription_type', 'profile']
    extra_kwargs = { 'password': {'write_only': True} } 

  def create(self, validated_data):
    profile_data = validated_data.pop('profile', None)
    password = validated_data.pop('password')

    user = User(**validated_data)
    user.set_password(password)
    user.save()

    if profile_data:
      Profile.objects.create(user=user, **profile_data)

    return user