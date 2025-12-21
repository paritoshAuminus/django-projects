from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# ------------------------------------------------------------------------
# for Authentication: BasicAuthentication and Permission: IsAuthenticated
# ------------------------------------------------------------------------

# @api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message': 'This is a public view accessible to everyone.'})

# @api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({'message': f'Hello, {request.user.username}, this view is private and is available to authenticated in users.'})


# ------------------------------------------------------------------------------------
# for Authentication: SessionAuthentication and Permission: IsAuthenticatedOrReadOnly
# ------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def blog_list(request):

    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            print(f'Request Header :: {request.headers}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# ------------------------------------------------------------------------
# for Authentication: TokenAuthentication and Permission: IsAuthenticated
# ------------------------------------------------------------------------

# api for authenticated users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        'is_staff': user.is_staff,
    })

# api for admin users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
    return Response({'message': f'Welcome to the admin panel, {request.user.username}'})


# -------------------------------------------------------------------------------
# for Authentication: JWTAuthentication and Permission: IsAuthenticatedOrReadOnly
# -------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
@permission_classes([JWTAuthentication])
def post_list(request):
    if request.method == 'GET':
        return Response({'message': 'Public can view this data.'})
    elif request.method =='POST':
        return Response({'message': f'Data created by: {request.user.username}'})