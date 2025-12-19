from rest_framework import serializers
from .models import Student


# This will convert the database data into json
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name', 'age', 'city']  # To include specific fields
        fields = '__all__'                  # To include all fields of db