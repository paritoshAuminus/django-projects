from rest_framework.generics import CreateAPIView
from .models import User, ConsultancyMember
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer 

class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]