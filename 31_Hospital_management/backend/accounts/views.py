from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User
from rest_framework.decorators import api_view, permission_classes

# Get user data
@api_view(["GET"])
def get_user(request):
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    return Response({"error": "User not found."}, status=status.HTTP_401_UNAUTHORIZED)

# User registration
@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not username:
        return Response({"error": "Please enter the username."}, status=status.HTTP_400_BAD_REQUEST)
    if not email:
        return Response({"error": "Please enter the email."}, status=status.HTTP_400_BAD_REQUEST)
    if not password:
        return Response({"error": "Please enter the password."}, status=status.HTTP_400_BAD_REQUEST)

    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    