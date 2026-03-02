from django.shortcuts import render
from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView

class BlogList(ListAPIView):
    queryset = Blog.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer

class RetrieveBlog(RetrieveAPIView):
    queryset = Blog.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer
 
