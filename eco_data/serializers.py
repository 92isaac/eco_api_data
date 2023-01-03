from rest_framework.serializers import ModelSerializer
from .models import Profile, Company
from django.contrib.auth.models import User




class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'