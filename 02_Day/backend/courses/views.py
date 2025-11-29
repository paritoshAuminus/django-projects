from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """
    API Endpoint which allows courses to be viewed or edited
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer