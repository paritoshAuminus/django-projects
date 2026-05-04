from rest_framework import serializers
from .models import User, ConsultancyMember

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ConsultancyMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConsultancyMember
        fields = ['user.username', 'user.email', 'consultancy', 'role']
