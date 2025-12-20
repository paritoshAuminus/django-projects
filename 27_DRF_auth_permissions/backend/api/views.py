from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Blog
from .serializers import BlogSerializer

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